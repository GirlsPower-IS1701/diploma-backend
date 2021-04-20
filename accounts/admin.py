from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)

    group.short_description = 'Groups'

    list_display = ('username', 'email', 'first_name', 'last_name', 'group')
admin.site.register(User, UserAdmin)