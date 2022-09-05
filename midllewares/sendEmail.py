from flask import request

from sweater import mail
from flask_mail import Message


def send_confirm_email(email, token, type):
    print("sending email")

    msg = Message("Confirm your email",
                  recipients=[email])
    if type == "confirm":
        msg.html = f"<a href={request.host_url}/user/confirm/{token}>Click here to confirm your email<a>"
    elif type == "repass":
        msg.html = f"<a href={request.host_url}/user/repass/{token}>Click here to confirm your email<a>"
    print(email)
    print(token)
    mail.send(msg)
