from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from .models import Vehicle, Arrive, Departure, Owner, VehicleTypes, VehicleColor, VehicleModelName, VehicleStatus


# Create your views here.


def show_all_vehicles(request):
    vehicles = Vehicle.objects.all()
    types = VehicleTypes.objects.all()
    model_names = VehicleModelName.objects.all()
    colors = VehicleColor.objects.all()
    owners = Owner.objects.all()
    return render(request, "all_vehicles.html", {"vehicles": vehicles,
                                                 "types": types,
                                                 "model_names": model_names,
                                                 "colors": colors,
                                                 "owners": owners,
                                                 })


def show_all_owners(request):
    owners = Owner.objects.all()
    return render(request, "all_owners.html", {"owners": owners})


def show_arrives(request):
    arriving_list = Arrive.objects.get_queryset().order_by('id')
    paginator = Paginator(arriving_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'arrives.html', {'page_obj': page_obj})


def show_departures(request):
    departure_list = Departure.objects.get_queryset().order_by('id')
    paginator = Paginator(departure_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'depatures.html', {'page_obj': page_obj})


def create_vehicle(request):
    if request.method == "POST":
        vehicle = Vehicle()
        vehicle.number = request.POST.get("number")
        vehicle.type = VehicleTypes.objects.get(id=request.POST.get("type"))
        vehicle.model_name = VehicleModelName.objects.get(id=request.POST.get("model_name"))
        vehicle.color = VehicleColor.objects.get(id=request.POST.get("color"))
        vehicle.owner = Owner.objects.get(id=request.POST.get("owner"))
        vehicle.status = VehicleStatus.objects.get(id=request.POST.get("status"))
        vehicle.info = request.POST.get("info")
        vehicle.save()
        return HttpResponseRedirect("/vehicle/")
    return render(request, "add_vehicle.html", {
        "types": VehicleTypes.objects.all(),
        "model_names": VehicleModelName.objects.all(),
        "colors": VehicleColor.objects.all(),
        "owners": Owner.objects.all(),
        "statuses": VehicleStatus.objects.all(),
    })


def create_owner(request):
    if request.method == "POST":
        owner = Owner()
        owner.name = request.POST.get("name")
        owner.surname = request.POST.get("surname")
        owner.middle_name = request.POST.get("middle_name")
        owner.tel = request.POST.get("tel")
        owner.email = request.POST.get("email")
        owner.info = request.POST.get("info")
        owner.save()
        return HttpResponseRedirect("/")
    return render(request, "add_owner.html")


def edit_vehicle(request, id):
    try:
        vehicle = Vehicle.objects.get(id=id)
        if request.method == "POST":
            print(vehicle.id)
            vehicle.number = request.POST.get("number")
            vehicle.type = VehicleTypes.objects.get(id=request.POST.get("type"))
            vehicle.model_name = VehicleModelName.objects.get(id=request.POST.get("model_name"))
            vehicle.color = VehicleColor.objects.get(id=request.POST.get("color"))
            vehicle.owner = Owner.objects.get(id=request.POST.get("owner"))
            vehicle.info = request.POST.get("info")
            if request.POST["in_parking"] == "yes":
                vehicle.in_parking = True
            else:
                vehicle.in_parking = False
            vehicle.status = VehicleStatus.objects.get(id=request.POST.get("status"))
            vehicle.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, 'edit_vehicle.html',
                          {"vehicle": vehicle,
                           "types": VehicleTypes.objects.all(),
                           "model_names": VehicleModelName.objects.all(),
                           "colors": VehicleColor.objects.all(),
                           "owners": Owner.objects.all(),
                           "statuses": VehicleStatus.objects.all(), })
    except Vehicle.DoesNotExist:
        return HttpResponseNotFound("Транспортное средство не найдено")


def edit_owner(request, id):
    try:
        owner = Owner.objects.get(id=id)
        if request.method == "POST":
            owner.name = request.POST.get("name")
            owner.surname = request.POST.get("surname")
            owner.middle_name = request.POST.get("middle_name")
            owner.tel = request.POST.get("tel")
            owner.email = request.POST.get("email")
            owner.info = request.POST.get("info")
            owner.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, 'edit_owners.html', {"owner": owner})
    except Owner.DoesNotExist:
        return HttpResponseNotFound("Нет такого владельца ТС")


def delete_vehicle(request, id):
    try:
        vehicle = Vehicle.objects.get(id=id)
        vehicle.delete()
        return HttpResponseRedirect("/")
    except Vehicle.DoesNotExist:
        return HttpResponseNotFound("Транспортное средство не найдено")


def delete_owner(request, id):
    try:
        owner = Owner.objects.get(id=id)
        owner.delete()
        return HttpResponseRedirect("/")
    except Owner.DoesNotExist:
        return HttpResponseNotFound("Владелец транспортного средства не найден")
