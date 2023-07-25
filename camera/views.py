from django.shortcuts import render

from .models import cam_in_start, cam_out_start, cam_stop


def start(request):
    if request.method == "POST":
        if request.POST.get("switch") == "1":
            cam_in_start()
            cam_out_start()
        else:
            cam_stop()
        return render(request, "camera.html")
    return render(request, "camera.html")
