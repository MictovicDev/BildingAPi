from django.core.mail import send_mail
from django.template.loader import render_to_string
import os
import logging


logger = logging.getLogger(__name__)


def send_linkmail(users_email,instance):
    try:
        subject = 'New Notification For You'
        email_data = {
            'title': instance.title,
            'time': instance.time,
            'category': instance.categories,
            'location' : instance.location
            }
        html_message = render_to_string('notifications/email.html',email_data)
        from_email = os.environ.get('EMAIL_USER')
        recipient_list = users_email
        send_mail(subject,
            message=None,
            from_email=from_email,
            recipient_list= recipient_list,
            fail_silently=False,
            html_message=html_message)
        print('sent')
        return from_email
    except Exception as e:
        logger.error(f"Email sending failed: {str(e)}")
