import re
import cv2
import easyocr
from datetime import datetime
from threading import Thread
from time import sleep
from scip.models import Vehicle, Arrive, Departure

# Create your models here.

"""
Cams config
"""
# ARRIVE_CAM = cv2.VideoCapture(0)
# DEPARTURE_CAM = cv2.VideoCapture(1)

#Video tests
ARRIVE_CAM = cv2.VideoCapture('vid.mp4')
DEPARTURE_CAM = cv2.VideoCapture('vid2.mp4')

thread_stop = False  # to stop cams

"""
CV config
"""
CV_MODEL = cv2.CascadeClassifier('plates.xml')

SCALE_FACTOR = 1.4
MIN_NEIGHBORS = 1
ALLOWLIST = '0123456789АВЕКМНОРСТУХ'
REGEX_PATTERN = r'^(([АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{1,2})(\d{2,3})|(\d{4}(?<!0000)[АВЕКМНОРСТУХ]{2})(\d{' \
                r'2})|(\d{3}(?<!000)(C?D|[ТНМВКЕ])\d{3}(?<!000))(\d{2}(?<!00))|([ТСК][АВЕКМНОРСТУХ]{2}\d{3}(?<!000))(' \
                r'\d{2})|([АВЕКМНОРСТУХ]{2}\d{3}(?<!000)[АВЕКМНОРСТУХ])(\d{2})|([АВЕКМНОРСТУХ]\d{4}(?<!0000))(\d{' \
                r'2})|(\d{3}(?<!000)[АВЕКМНОРСТУХ])(\d{2})|(\d{4}(?<!0000)[АВЕКМНОРСТУХ])(\d{2})|([АВЕКМНОРСТУХ]{' \
                r'2}\d{4}(?<!0000))(\d{2})|([АВЕКМНОРСТУХ]{2}\d{3}(?<!000))(\d{2,3})|(^Т[АВЕКМНОРСТУХ]{2}\d{3}(' \
                r'?<!000)\d{2,3}))'
LANGUAGE = 'ru'

"""
Gate config
"""
GATE_WAIT_TIME = 30


def start_cam(cam, where, cv_model=CV_MODEL, allow_list=ALLOWLIST, regex=REGEX_PATTERN, sf=SCALE_FACTOR,
              mn=MIN_NEIGHBORS, lang=LANGUAGE):
    global thread_stop
    thread_stop = False
    crop_img = None

    while thread_stop is False:
        _, image = cam.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        plates = cv_model.detectMultiScale(gray, scaleFactor=sf, minNeighbors=mn)
        now = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

        if len(plates) > 0:
            for x, y, width, height in plates:
                cv2.rectangle(gray, (x, y), (x + width, y + height), (0, 0, 255), thickness=5)
                crop_img = gray[y:y + height, x:x + width]

            text = easyocr.Reader([lang])
            text = text.readtext(crop_img, allowlist=allow_list, detail=0)

            try:
                if re.fullmatch(regex, text[0]):
                    img_name = f"{text[0]}_{now}.png"
                    if Vehicle.objects.filter(number=text[0], in_parking=False,
                                              status=2).exists() and where == "arrival":
                        vehicle = Vehicle.objects.get(number__contains=text[0])
                        vehicle.in_parking = True
                        vehicle.save()
                        arrive = Arrive()
                        arrive.vehicle = vehicle
                        arrive.save()
                        cv2.imwrite(img_name, gray)
                        open_gate()
                    elif Vehicle.objects.filter(number=text[0], in_parking=True,
                                                status=2).exists() and where == "departure":
                        vehicle = Vehicle.objects.get(number__contains=text[0])
                        vehicle.in_parking = False
                        vehicle.save()
                        departure = Departure()
                        departure.vehicle = vehicle
                        departure.save()
                        cv2.imwrite(img_name, gray)
                        open_gate()
            except IndexError:
                pass


def cam_in_start():
    global thread_stop
    thread_stop = False
    t = Thread(target=start_cam, args=(ARRIVE_CAM, "arrival"), name="cam_arrival")
    t.start()



def cam_out_start():
    global thread_stop
    thread_stop = False
    t = Thread(target=start_cam, args=(DEPARTURE_CAM, "departure"), name="cam_departure")
    t.start()



def cam_stop():
    global thread_stop
    thread_stop = True


def open_gate():
    """
    Imitation of gate
    """
    sleep(GATE_WAIT_TIME)
