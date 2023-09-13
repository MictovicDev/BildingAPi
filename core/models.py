from django.db import models
from authentication.models import *

# Create your models here.




class Project(models.Model):
    CATEGORIES = (
    ('Skilledlabour', 'SL'),
    ('Supplier', 'SU')
    )

    SCOPE = (
        ('Small', 'SM'),
        ('Medium', 'MD'),
        ('Large', 'LG')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=False, null=False)
    categories = models.CharField(max_length=500,choices=CATEGORIES)
    skills = models.CharField(max_length=500,blank=False, null=False)
    scope = models.CharField(max_length=500, choices=SCOPE, blank=False, null=False)
    experience = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    location = models.CharField(max_length=1000)
    budget = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    # image = models.ForeignKey('Images',on_delete=models.CASCADE,null=True,related_name='owner')
    description = models.TextField()


    def __str__(self):
        return f"{self.owner.firstname} project"



class Request(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # url = models.URLField(null=True)
    title = models.CharField(max_length=250)
    category= models.TextField()
    location = models.TextField()
    budget = models.BigIntegerField()
    
    
    description = models.TextField()
    

    def __str__(self):
        return f"{self.owner.firstname} request's"
    


class Item(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField(default=0)
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='items',null=True)
    

    
    
class ProjectImage(models.Model):
    image = models.FileField(upload_to='files/', null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='images',null=True )
   


    def __str__(self):
        return self.image.url
    
class RequestImage(models.Model):
    image = models.FileField(upload_to='files/', null=True)
    supplierapplication = models.ForeignKey('SuppliersApplication', on_delete=models.CASCADE, related_name='images',null=True)
    request= models.ForeignKey(Request, on_delete=models.CASCADE, related_name='images', null=True)
   
   


    def __str__(self):
        return self.image.url

class Store(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=500)
    address = models.TextField()
    category = models.TextField()
    image = models.ImageField(upload_to=True)
    document = models.FileField(upload_to='Files/')


    def __str__(self):
        return F"{self.name}'s Store" 
    
    
class BidForProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    applicant = models.OneToOneField(User, on_delete=models.CASCADE,related_name='applic')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.firstname} bidded for this project"
    
class SuppliersApplication(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE,null=True)
    request = models.OneToOneField(Request, on_delete=models.CASCADE)
    letter = models.TextField()


    def __str__(self):
        return f"{self.store.name} applied to supply this goods"



    

    


    

