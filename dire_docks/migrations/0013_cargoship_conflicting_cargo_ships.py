# Generated by Django 4.0.3 on 2022-03-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dire_docks', '0012_cargoship_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargoship',
            name='conflicting_cargo_ships',
            field=models.ManyToManyField(to='dire_docks.cargoship'),
        ),
    ]