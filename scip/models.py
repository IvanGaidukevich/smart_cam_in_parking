from django.db import models


# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True)
    surname = models.CharField(max_length=40)
    tel = models.CharField(max_length=12)
    email = models.EmailField()
    info = models.CharField(max_length=100, null=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name} {self.surname}'


class VehicleTypes(models.Model):
    type_name = models.CharField(max_length=10)
    info = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return f'{self.type_name}'


class VehicleModelName(models.Model):
    model_name = models.CharField(max_length=40)
    info = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return f'{self.model_name}'


class VehicleColor(models.Model):
    color1 = models.CharField(max_length=20)
    info = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.color1}'


class VehicleStatus(models.Model):
    status = models.CharField(max_length=20)
    info = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.status}'


class Vehicle(models.Model):
    number = models.CharField(max_length=9)
    type = models.ForeignKey(VehicleTypes, on_delete=models.CASCADE)
    model_name = models.ForeignKey(VehicleModelName, on_delete=models.CASCADE)
    color = models.ForeignKey(VehicleColor, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    status = models.ForeignKey(VehicleStatus, on_delete=models.CASCADE)
    info = models.CharField(max_length=100)
    in_parking = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return f'{self.number} {self.model_name} {self.color}'


class Arrive(models.Model):
    time = models.DateTimeField(auto_now=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return f'{self.time} {self.vehicle}'


class Departure(models.Model):
    time = models.DateTimeField(auto_now=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return f'{self.time} {self.vehicle}'
