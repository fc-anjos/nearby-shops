# Generated by Django 3.0.7 on 2020-06-26 19:33
from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'comercio.json'

def load_data(apps, schema_editor):
    Shop = apps.get_model('shops', 'Shop')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects['features']:
            if obj['geometry']['type'] == 'Point':
                try:
                    coordinates = obj['geometry']['coordinates']
                    latitude = coordinates[0]
                    longitude = coordinates[1]
                    name = obj['properties']['name']
                    location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
                    Shop(name=name, location = location).save()
                except:
                    pass

class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]