from django.core.mail import send_mail


def send_linkmail(user, token):
    token = str(token)
    tokencheck = token
    url = f"http://localhost:8000/auth/activation/{tokencheck}"
    subject = 'Welcome to Your Bilding'
    message = f"Thanks for Registering on bilding {user.firstname}, click the link below to verify your account, {url}"
    from_email = 'awaemekamichael@gmail.com'  # Replace with your email
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)


