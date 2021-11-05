from django.contrib import admin
from dashboard import models


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['number', 'added_on']


admin.site.register(models.Device, DeviceAdmin)


class DeviceReadingAdmin(admin.ModelAdmin):
    list_display = ['device', 'message_type', 'reading', 'device_voltage', 'added_on']


admin.site.register(models.DeviceReading, DeviceReadingAdmin)
