# Generated by Django 4.0.3 on 2022-03-07 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dire_docks', '0009_rename_cargo_ship_a_cargoshipconflict_cargo_ship_a_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargoship',
            old_name='dock_id',
            new_name='dock',
        ),
        migrations.RenameField(
            model_name='cargoshipconflict',
            old_name='cargo_ship_a_id',
            new_name='cargo_ship_a',
        ),
        migrations.RenameField(
            model_name='cargoshipconflict',
            old_name='cargo_ship_b_id',
            new_name='cargo_ship_b',
        ),
    ]
