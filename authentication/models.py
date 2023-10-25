from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin)
import uuid
from .managers import UserManager
# from core.models import Project



# from django_phonenumbers import PhoneNumber


class User(AbstractBaseUser, PermissionsMixin):

    COUNTRY_CHOICES = (
        ('Algeria', 'Algeria'),
        ('Nigeria', 'Nigeria'),
        ('Egypt', 'Egypt'),
        ('South Africa', 'South Africa'),
        ('Morocco', 'Morocco'),
        ('Kenya', 'Kenya'),
        ('Ethiopia', 'Ethiopia'),
        ('Ghana', 'Ghana'),
        ('Cameroon', 'Cameroon'),
        ('Ghana', 'Ghana'),
        ('Tanzania', 'Tanzania'),
        ('Cote d\'Ivoire', 'Cote d\'Ivoire'),
        )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=500,blank=True, null=True)
    phone_number = models.PositiveBigIntegerField(null=True)
    lastname = models.CharField(max_length=500)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=50, blank=True, null=True,unique=False)
    role = models.CharField(max_length= 250, blank=True,null=True)
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=250, null=True)
    token = models.CharField(max_length=500, blank=True, null=True)
    updates = models.BooleanField(default=False)
    authMedium = models.CharField(max_length=50, default='email')
    profile_pics = models.ImageField(upload_to='files/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    profession = models.CharField(max_length=500,blank=True, null=True)
    hires = models.PositiveIntegerField(default=0)
    # hired = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname','role','phone_number','country']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bvn = models.PositiveBigIntegerField(blank=False, null=True)
    gov_id_image = models.FileField(upload_to='files/', blank=True ,null=True)
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)

class ChangePassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    oldpassword = models.CharField(max_length=500, blank=True, null=True)
    newpassword = models.CharField(max_length=500, blank=True,null=True)

        
class Favourites(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='favourites_owner')
    favourite = models.ManyToManyField(User, related_name='favourites')










