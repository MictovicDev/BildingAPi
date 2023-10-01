from django.db import models
from authentication.models import *
from rest_framework import reverse

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
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    url = models.CharField(max_length=250, null=True,blank=True)
    
    # recent_projects = models.ManyToManyField('RecentProject', related_name='projects')
    
    def get_absolute_url(self):
        return reverse('projectdetail', args=[str(self.pk)])

    def __str__(self):
       return ''

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
    title = models.CharField(max_length=250)
    category= models.CharField(max_length=500, choices=CATEGORIES)
    location = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title
    


class RequestImage(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    request= models.ForeignKey(Request, on_delete=models.CASCADE, related_name='images',blank=True, null=True) 

    # def __str__(self):
    #     return self.image.path


class Item(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField(default=1)
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='items',null=True)

    def __str__(self):
        return self.name
    

    
    
# class ProjectImage(models.Model):
#     image = models.ImageField(upload_to='images/', default='bilding/media/images/IMG_4701.jpg')
#     project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='images',null=True)

class Store(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True,related_name='store')
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    logo = models.ImageField(upload_to=True)
    document = models.FileField(upload_to='Files/')


    def __str__(self):
        return F"{self.name}'s Store" 
    
    
class BidForProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE,related_name='applic')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.firstname} bidded for this project"
    
class SuppliersApplication(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE,null=True)
    request = models.OneToOneField(Request, on_delete=models.CASCADE)
    letter = models.TextField()


    def __str__(self):
        return f"{self.store.name} applied to supply this goods"



    

    


    

