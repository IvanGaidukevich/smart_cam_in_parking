# Generated by Django 4.2.2 on 2023-07-24 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='info',
            field=models.CharField(max_length=100, null=True),
        ),
    ]