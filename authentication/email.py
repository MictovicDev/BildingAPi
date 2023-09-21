from django.core.mail import send_mail


def send_linkmail(user, token):
    token = str(token)
    tokencheck = token
    url = f"http://localhost:8000/auth/activation/{tokencheck}"
    subject = 'Welcome to Bilding Construction'
    name = user.firstname.capitalize()
    message = f"Thanks for Registering on bilding {name}, Click the link below to verify your account, {url}"
    from_email = 'bildingconstruction@gmail.com'  # Replace with your email
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)


