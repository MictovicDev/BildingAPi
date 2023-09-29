import smtplib

try:
    server = smtplib.SMTP('bilding@getbilding.com', 26)
    server.starttls()
    server.login('bilding@getbilding.com', 'secureBILDING02@')
    server.quit()
    print("SMTP connection successful")
except Exception as e:
    print("SMTP connection failed:", str(e))
