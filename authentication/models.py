from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin)
import uuid
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=500,)
    phone_number = models.IntegerField(blank=True, null=True)
    lastname = models.CharField(max_length=500)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    address = models.TextField(default='shofunwa')
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=50, blank=True, null=True,unique=False)
    role = models.CharField(max_length= 250,blank=True,null=True)
    location = models.CharField(max_length=250,blank=True, null=True)
    token = models.CharField(max_length=500, blank=True, null=True)
    bvn = models.BigIntegerField(blank=False, null=True)
    hires = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/',null=True)
    
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname','role','phone_number','location']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin