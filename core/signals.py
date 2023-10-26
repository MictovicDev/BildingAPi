from django.db.models.signals import post_save
from authentication.models import *
from django.dispatch import receiver
from core.models import *

@receiver(post_save, sender=Project)
def create_workernotification(sender, instance, created, **kwargs):
    print(kwargs.get('signal'))
    if created:
        user = instance.owner
        message = f"A new Project {instance.title} has been created by {user}"
        WorkerNotification.objects.create(user=user, message=message)


@receiver(post_save, sender=BidForProject)
def create_buildernotification(sender, instance, created, **kwargs):
    if created:
        user = instance.project.owner
        message = f"{instance.applicant.firstname} applied for your project"
        BuilderNotification.objects.create(user=user, message=message)

@receiver(post_save, sender=Request)
def create_suppliernotification(sender, instance, created, **kwargs):
    if created:
        user = instance.owner
        message = f"A new Request {instance.title} has been created by {user}"
        SupplierNotification.objects.create(user=user, message=message)




        