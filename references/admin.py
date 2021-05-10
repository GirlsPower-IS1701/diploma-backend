from django.contrib import admin
from .models import Reference_Type, Reference


class ReferenceTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reference_Type, ReferenceTypeAdmin)


class ReferenceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reference, ReferenceAdmin)
