from django.core.mail import send_mail
from django.template.loader import render_to_string
import os
# from celery import shared_task
# from django_celery_email.models import Email



# @shared_task
def send_linkmail(user, token):
    token = str(token)
    tokencheck = token
    url = f"http://localhost:8000/auth/activation/{tokencheck}"
    subject = 'Welcome to Bilding Construction'
    name = user.firstname.capitalize()
    email_data = {
        'url': url,
        'token': tokencheck,
        'name': name
    }
    html_message = render_to_string('authentication/email.html',email_data)
    from_email = os.environ.get('EMAIL_USER')
    recipient_list = [user.email]
    send_mail(subject,
        message=None,
        from_email=from_email,
        recipient_list= recipient_list,
        fail_silently=False,
        html_message=html_message,)
    return name


