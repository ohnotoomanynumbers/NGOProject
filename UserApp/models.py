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
ROLE_CHOICES =(
    ("admin", "admin"),
    ("user", "user"),
    )
class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, firstName, lastName, role, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
            
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, firstName, lastName, role, password, **other_fields)

    def create_user(self, email, username, firstName, lastName, role, password, **other_fields):
        if not username:
            raise ValueError(_('You must provide a user name'))
        if not email:
            raise ValueError(_('You must provide an email address'))
        if not password:
            raise ValueError(_('You must provide an password'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          firstName=firstName, lastName=lastName, role=role, **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    firstName=models.CharField(max_length=40)
    lastName=models.CharField(max_length=40)
    role=models.CharField(max_length=40, default="user", choices = ROLE_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()
    #USERNAME_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email", "firstName", "lastName", "role"]

    def __str__(self):
        return self.username

