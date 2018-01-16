"""siteall2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app1.views import prjStateA
from app1.views import prjStateI
from app1.views import index
from app1.views import csv
from app1.views import top
from app1.views import roc
from app1.views import blank
from app1.views import maps
from app1.views import chart1
from app1.views import chart2
from app1.views import chart3
from app1.views import profile
from app1.views import obesityCharts
from app1.views import obesityCharts3
from app1.views import obesityCharts103
from app1.views import obesityCharts104
from app1.views import index2
from app1.views import populationCharts
from app1.views import populationCharts2
from app1.views import obesityMaps
from app1.views import populationMaps
from app1.views import test
from app1.views import home
from app1.views import obesityCharts2
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', home),
    url(r'^prjStateA/', prjStateA),
    url(r'^prjStateI/', prjStateI),
    url(r'^index/', index),
    url(r'^csv/', csv),
    url(r'^top/', top),
    url(r'^roc/', roc),
	url(r'^test/', test),
    url(r'^blank/', blank),
    url(r'^maps/', maps),
    url(r'^chart1/', chart1),
    url(r'^chart2/', chart2),
    url(r'^chart3/', chart3),
    url(r'^profile/', profile),

    url(r'^obesityCharts/', obesityCharts),
	url(r'^obesityCharts2/', obesityCharts2),
	url(r'^obesityCharts3/', obesityCharts3),
    url(r'^obesityCharts103/', obesityCharts103),
    url(r'^obesityCharts104/', obesityCharts104),
    url(r'^populationCharts/', populationCharts),
	url(r'^populationCharts2/', populationCharts2),
    url(r'^index2/', index2),
    url(r'^obesityMaps/', obesityMaps),
    url(r'^populationMaps/', populationMaps),


]
