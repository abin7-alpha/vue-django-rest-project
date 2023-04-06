import urllib
import requests
import json
import sendgrid

from codework import settings

from authorization.models import Account
from authorization.serializers import AccountSerializer


def url_encode(word):
    new_word = urllib.parse.quote(word.encode('utf-8'), safe='')
    return new_word


def get_token(username, password, redirect_uri):
    url = f"http://127.0.0.1:8000/api-auth/token/"

    client_info = f'client_id={settings.CLIENT_ID}&client_secret={settings.CLIENT_SECRET}&grant_type=password'
    redirect_uri = f'&redirect_uri={url_encode(redirect_uri)}'
    user_info = f'&username={url_encode(username)}&password={url_encode(password)}'
    payload = client_info + user_info + redirect_uri

    headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)

    return data


def send_registration_email(email):
    sg = sendgrid.SendGridClient(settings.SENDGRID_API_KEY)
    mail = sendgrid.Mail()
    mail.add_to(email)

    mail.set_subject("Welcome CodeWork User")
    msg = """<html>
                <head>
                </head>
                <body align="left" style="color:black">
                    <h1>Code Work</h1>
                    <p>Dear User, We welcomes you </p>
                    <br><br>Regards,<br>
                    Team CodeWork<br>
                </body>
            </html>
          """
    mail.set_html(msg)
    mail.set_from(settings.SENDER_EMAIL)
    status, msg = sg.send(mail)
    return status, msg


def serialized_user(email):
    user = Account.objects.get(email=email)
    serializer = AccountSerializer(user)
    data = serializer.data
    return data


def post_register(email):
    data = serialized_user(email)
    send_registration_email(email)
    return data
