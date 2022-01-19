from django.contrib import admin
from .models import *
admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(SensorDetails)
admin.site.register(SensorRepairLog)
admin.site.register(TrackingLog)
# Register your models here.
