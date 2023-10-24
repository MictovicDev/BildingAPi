from django.db.models.signals import post_save
from authentication.models import *
from django.dispatch import receiver
from core.models import Project, Request, Notification, Store

@receiver(post_save, sender=Project)
def create_notification(sender, instance, created, **kwargs):
    if created:
        user = instance.owner
        message = f"A new Project {instance.title} has been created by {user}"
        Notification.objects.create(user=user, message=message)

# @receiver(post_save, sender=User)
# def create_notification(sender, instance, created, **kwargs):
#      role = instance.role
#      if role == 'SupplierRole':
#         Store.objects.create(owner=)
#         message = f"A new Project {instance.title} has been created by {user}"
#         Notification.objects.create(user=user, message=message)