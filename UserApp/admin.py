from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'username', 'firstName', "lastName", "role")
    #list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    list_filter = ('email', 'username', 'firstName', "role")
    ordering = ('email',)
    list_display = ('email', 'username', 'firstName', "lastName", "role")
    fieldsets = (
        (None, {'fields': ('email', 'username', 'firstName', "lastName", "role")}),
        #('Permissions', {'fields': ('is_staff', 'is_active')}),
        #('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        #CustomUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            #'fields': ('email', 'user_name', 'firstName', 'password1', 'password2', 'is_active', 'is_staff')
            'fields': ('email', 'username', 'firstName', "lastName", "role", 'password1', 'password2',)
            }
         ),
    )


admin.site.register(CustomUser, UserAdminConfig)