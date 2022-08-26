from sweater import mail
from flask_mail import Message


def send_confirm_email(email, token):
    print("sending email")
    msg = Message("Confirm your email",
                  recipients=[email])
    msg.html = f"<a href=192.168.0.106/user/confirm/{token}>Click here to confirm your email<a>"
    print(email)
    print(token)
    mail.send(msg)
