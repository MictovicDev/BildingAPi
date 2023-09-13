from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)
import uuid

class UserManager(BaseUserManager):
    def create_user(self,email,firstname,lastname,role,phone_number,password=None):
       if not (email):
           raise ValueError('User must have an email address')
       
       email = self.normalize_email(email)
       user = self.model(email=self.normalize_email(email),firstname=firstname,
                         lastname=lastname,
                         role=role,
                         phone_number=phone_number)
       
       user.set_password(password)
       user.is_active = True
    #    print(password)
       user.save(using=self.db)
       return user
        

     
#https://localhost:8000/oauth/complete/google-oauth2/
    def create_superuser(self, email,firstname, lastname,role,phone_number, password=None):
        user = self.create_user(email, firstname, lastname,role,phone_number, password)
        user.is_admin=True
        
        user.save(using=self.db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    CATEGORIES = (
    ('CO', 'Contractor'),
    ('SU', 'Supplier'),
    ('WO', 'Worker'),
    )

    LOCATION = (
        ('ABJ', 'Abuja'),
        ('ABA', 'Aba'),
        ('AKR', 'Akure'),
        ('BNI', 'Benin City'),
        ('CAL', 'Calabar'),
        ('ENU', 'Enugu'),
        ('IBD', 'Ibadan'),
        ('ILR', 'Ilorin'),
        ('JOS', 'Jos'),
        ('KAD', 'Kaduna'),
        ('KAN', 'Kano'),
        ('LAG', 'Lagos'),
        ('MAI', 'Maiduguri'),
        ('OWE', 'Owerri'),
        ('PHC', 'Port Harcourt'),
        ('SKT', 'Sokoto'),
        ('UYO', 'Uyo'),
        ('WRR', 'Warri'),
        ('ONI', 'Onitsha'),
        ('OSB', 'Osogbo'),

    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=500,)
    phone_number = models.IntegerField()
    lastname = models.CharField(max_length=500)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=50, blank=True, null=True,unique=False)
    role = models.CharField(max_length= 250,choices=CATEGORIES, blank=False, null=False)
    location = models.CharField(max_length=250, choices=LOCATION,blank=True, null=True)
    bvn = models.BigIntegerField(blank=False, null=True)
    hires = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/',null=True)
    
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname','phone_number','role',]

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin