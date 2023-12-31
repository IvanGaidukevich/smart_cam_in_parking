# Generated by Django 4.2.2 on 2023-07-24 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20, null=True)),
                ('surname', models.CharField(max_length=40)),
                ('tel', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color1', models.CharField(max_length=20)),
                ('info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=40)),
                ('info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=10)),
                ('info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=9)),
                ('info', models.CharField(max_length=100)),
                ('in_parking', models.BooleanField(default=False)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scip.vehiclecolor')),
                ('model_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scip.vehiclemodelname')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scip.owner')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scip.vehiclestatus')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scip.vehicletypes')),
            ],
        ),
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scip.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Arrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scip.vehicle')),
            ],
        ),
    ]
