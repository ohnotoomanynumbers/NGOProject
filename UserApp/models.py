from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName=models.CharField(max_length=40)
    lastName=models.CharField(max_length=40)
    role=models.CharField(max_length=40, default="user")
    email=models.CharField(max_length=999, default='None')

    def __str__(self):
        return f'{self.user.username} Profile'
"""
class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, firstName, lastName, password, **other_fields):
        #other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        #other_fields.setdefault('is_active', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(self, email, user_name, firstName, password, **other_fields)

    def create_user(self, email, user_name, firstName, lastName, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        if not password:
            raise ValueError(_('You must provide an password'))
        #email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          firstName=firstName, lastName=lastName, **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    firstName=models.CharField(max_length=40)
    lastName=models.CharField(max_length=40)
    role=models.CharField(max_length=40, default="user")
    #is_active = models.BooleanField(default=False)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', "firstName", "lastName"]

    def __str__(self):
        return self.user_name

