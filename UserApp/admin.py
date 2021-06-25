from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'user_name', 'firstName', "lastName")
    #list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    list_filter = ('email', 'user_name', 'firstName')
    ordering = ('email',)
    list_display = ('email', 'user_name', 'firstName', "lastName")
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'firstName', "lastName")}),
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
            'fields': ('email', 'user_name', 'firstName', "lastName", 'password1', 'password2',)
            }
         ),
    )


admin.site.register(CustomUser, UserAdminConfig)