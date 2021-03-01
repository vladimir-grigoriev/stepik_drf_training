from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'middle_name',
                    'phone',
                    'adress'
                ),
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)
