# Generated by Django 4.0.3 on 2022-03-09 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dire_docks', '0011_cargoshipconflict_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargoship',
            name='type',
            field=models.CharField(choices=[('RED', 'Red'), ('BLUE', 'Blue'), ('GREEN', 'Green')], default='RED', max_length=100),
            preserve_default=False,
        ),
    ]
