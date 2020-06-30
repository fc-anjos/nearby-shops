from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.serializers import serialize
from .models import Shop

def points_view(request):
    points_as_geojson = serialize('geojson', Shop.objects.all())
    return HttpResponse(points_as_geojson, content_type='json')

class MainPageView(TemplateView):
    template_name = 'shops/index.html'
