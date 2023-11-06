from django.db.models.signals import post_save
from core.models import *
from django.dispatch import receiver
from authentication.models import User
from . import emails


# users = User.objects.filter(updates=True)
# users = User.objects.all()
# users_email = [user.email for user in users]


# @receiver(post_save, sender=Project)
# def send_updates(sender, instance, created, **kwargs):
#     print(kwargs.get('signal'))
#     if created:
#         emails.send_linkmail(users_email, instance)
#         print('yes')
        
       