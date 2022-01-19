"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mirai import views
from django.urls import include
from django.views.generic.base import TemplateView
from django.conf import settings 
from django.conf.urls.static import static 
from mirai.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #Company paths 
    path('comp', views.comp),
    path('show', views.show),
    path('edit/<str:cName>', views.edit),
    path('update/<str:cName>', views.update),
    path('delete/<str:cName>', views.delete), 

    #employee paths
    path('emp', views.emp),
    path('home', views.home),
    path('showemp', views.showemp),
    path('deleteEmp/<str:eID>', views.deleteEmp),
    path('editemp/<str:eID>', views.editemp), 
    path('updateEmp/<str:eID>', views.updateEmp),
    path('drug/', views.drugtest),
    path('showdrugtest/', views.showdrugtest),

    #home paths
    path('emphome/', views.emphome),
    path('sensorhome/', views.sensorhome),
    path('trackhome/', views.trackhome),

    
    #sensor paths
    path('sensor/', views.sensor),
    path('showsensor/', views.showsensor),
    path('deleteSensor/<str:sID>', views.deleteSensor),
    path('editSensor/<str:sID>', views.editSensor), 
    path('updateSensor/<str:sID>', views.updateSensor),
    path('repairlog/<str:sID>' ,views.repairlog),
    path('editrepairlog/<str:sID>', views.editRepairLog), 
    path('updateRepairLog/<str:sID>', views.updateRepairLog),
    path('showrepairlog/', views.showrepairlog),
    path('trackinglog/' ,views.trackinglog),
    path('showtrackinglog/' ,views.showtrackinglog),

    

    #Homepage path
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    #inbuilt login path
    path('accounts/', include('django.contrib.auth.urls')),
]
#for Media Storage 
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 