from django.contrib import admin

from rules.contrib.admin import ObjectPermissionsModelAdmin

from zezere.models import Device, RunRequest, SSHKey


class RunRequestAdmin(ObjectPermissionsModelAdmin):
    pass


class DeviceAdmin(ObjectPermissionsModelAdmin):
    pass

class SSHKeyAdmin(ObjectPermissionsModelAdmin):
    pass

admin.site.register(RunRequest, RunRequestAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(SSHKey, SSHKeyAdmin)
