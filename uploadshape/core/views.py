import simplejson

import zipfile
from subprocess import call
from os import path, mkdir
from datetime import datetime
from shutil import rmtree

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.gis.geos import Polygon

from .forms import UploadFileForm
from .models import Shape


def handle_uploaded_file(file, user):
    upload_folder = 'media/'
    upload_path = path.join(upload_folder,
        user.username + datetime.now().strftime('%f')
        )
    imported_polygons = 0

    if zipfile.is_zipfile(file):
        zip = zipfile.ZipFile(file)
        for filename in zip.namelist():
            if filename[-3:].lower() == 'shp':
                mkdir(upload_path)
                zip.extractall(upload_path)
                call(['ogr2ogr',
                    '-f', 'GeoJSON',
                    '-t_srs', 'EPSG:4674',
                    path.join(upload_path, filename[:-3] + 'geojson'),
                    path.join(upload_path, filename)
                    ])

                data_json = open(
                    path.join(upload_path, filename[:-3] + 'geojson'), 'r'
                    ).read()
                data = simplejson.loads(data_json)
                for feature in data['features']:
                    if feature['geometry'].get('type') == 'Polygon':
                        shape = Shape(
                            polygon=Polygon(feature['geometry']['coordinates'][0]),
                            user=user
                            )
                        shape.save()
                        imported_polygons += 1

                rmtree(upload_path)
                msg = 'Imported %s polygons' % imported_polygons
            else:
                msg = 'We did not find a shape file in the zip file.'
    else:
        msg = 'UploadedFile is not a valid zip file.'


def upload_file(request):
    '''View that renders and processes the upload files form.'''

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['upload_file'], request.user)
            return HttpResponseRedirect('/upload-success/')
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})
