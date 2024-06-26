from django.db import models
# from authentication.models import *
from rest_framework import reverse
from django.contrib.auth import get_user_model
from authentication.models import *

User = get_user_model()

# Create your models here.
class Project(models.Model):
    CATEGORIES = (
      ('Electrical', 'Electrical'),
      ('Plumbing', 'Plumbing'),
      ('Construction', 'Construction'),
      ('Plastering', 'Plastering'),
      ('Painting', 'Painting'),
      ('InteriorDecoration', 'InteriorDecoration')
      )

    SCOPE = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large')
    )
    EXPERIENCE = (
        ('1-3yrs', '1-3yrs'),
        ('4-8yrs', '4-8yrs'),
        ('10-15yrs', '10-15yrs')
    )
    DURATION = (
        ('1-6months', '1-6months'),
        ('1-2yrs', '1-2yrs'),
        ('1-5yrs', '1-5yrs')
    )
    SKILLS = (
        ('Engineer', 'Engineer'),
        ('Electrician', 'Electrician'),
        ('Contractor', 'Contractor'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=True, null=True)
    categories = models.CharField(max_length=500,choices=CATEGORIES, blank=True, null=True)
    skills = models.CharField(max_length=500,choices=SKILLS, blank=True, null=True)
    scope = models.CharField(max_length=500, choices=SCOPE, blank=True, null=True)
    experience = models.CharField(max_length=500, default=0, choices=EXPERIENCE, blank=True, null=True)
    duration = models.CharField(max_length=500, default=0, choices=DURATION,  blank=True, null=True)
    location = models.CharField(max_length=1000,blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to='projectimages/', blank=True, null=True)
    image2 = models.ImageField(upload_to='projectimages/', blank=True, null=True)
    time = models.TimeField(auto_now_add=True, blank=True, null=True)
    url = models.CharField(max_length=250, null=True,blank=True)
    


    class Meta:
        ordering = ['-time']

    def __str__(self):
       return self.title


class RecentProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name='projects')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.project.title}"

    
    
class Request(models.Model):
    CATEGORIES = (
      ('Electrical', 'Electrical'),
      ('Plumbing', 'Plumbing'),
      ('Construction', 'Construction'),
      ('Plastering', 'Plastering'),
      ('Painting', 'Painting'),
      ('InteriorDecoration', 'InteriorDecoration')
      )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=True, null=True)
    category= models.CharField(max_length=500, choices=CATEGORIES, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to='Requestimages/', blank=True, null=True)
    image2 = models.ImageField(upload_to='Requestimages/', blank=True, null=True)
    time = models.TimeField(auto_now_add=True, blank=True, null=True)


    class Meta:
        ordering = ['-time']


    def __str__(self):
        return self.title

class Store(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True,related_name='store')
    name = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=500, blank=True, null=True)
    logo = models.ImageField(upload_to=True, blank=True,null=True)
    document = models.FileField(upload_to='Files/',blank=True, null=True)


    def __str__(self):
        return F"{self.owner.email}'s Store" 
    
class SuppliersApplication(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE,null=True, blank=True)
    myrequest = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='myrequest', blank=True, null=True)
    letter = models.TextField(blank=True, null=True)
    delivery_inclusive = models.BooleanField(default=False)
    time = models.TimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to='ApplicationImages/', blank=True, null=True)
    accepted = models.BooleanField(default=False)
    


    def __str__(self):
        return f"{self.store.name} applied to supply this goods"
    

class BidItem(models.Model):
    amount = models.IntegerField(default=0)
    supplier_bid = models.ForeignKey(SuppliersApplication,related_name='biditem', on_delete=models.CASCADE, blank=True, null=True)
    


    # def __str__(self):
    #     return

class Item(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField(default=1)
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='items',null=True)
    

    def __str__(self):
        return self.name
    

     
class BidForProject(models.Model):
    DURATION = (
        ('1-6months', '1-6months'),
        ('1-2yrs', '1-2yrs'),
        ('1-5yrs', '1-5yrs')
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE,blank=True, null=True, related_name='bids')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE,related_name='applicant', blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    duration = models.CharField(max_length=500, choices=DURATION, blank=True, null=True)
    applicationletter = models.TextField(blank=True, null=True)
    images = models.ImageField(upload_to='Resume/',blank=True, null=True)
    time = models.TimeField(auto_now_add=True,blank=True,null=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.applicant.lastname} bidded for this project"
    

   


class Reviews(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', blank=True, null=True)
    reviewed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewed',blank=True,null=True)
    content = models.TextField(blank=True, null=True)
    stars = models.PositiveIntegerField(null=True, blank=True)
    time = models.TimeField(auto_now_add=True, blank=True, null=True)



class Notification(models.Model):
    read = models.BooleanField(default=False, blank=True, null=True)
    time_stamp = models.TimeField(auto_now_add=True, blank=True, null=True)


    class Meta:
        abstract = True
    
class BuilderNotification(Notification):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buildernotifications')
    message = models.CharField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.message
    
class WorkerNotification(Notification):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workernotifications')
    message = models.CharField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.message
    
class SupplierNotification(Notification):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suppliernotifications')
    message = models.CharField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.message
    

    
