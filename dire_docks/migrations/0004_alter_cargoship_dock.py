# Generated by Django 4.0.3 on 2022-03-06 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dire_docks', '0003_rename_dock_id_cargoship_dock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargoship',
            name='dock',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='dire_docks.dock'),
        ),
    ]