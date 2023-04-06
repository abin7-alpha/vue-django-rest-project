import sendgrid

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser
from django.dispatch import receiver

from authorization.managers import MyaccountManager
from codework import settings


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=150, verbose_name="first_name", blank=True)
    last_name = models.CharField(max_length=150, verbose_name="last_name", blank=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyaccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


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


@receiver(post_save, sender=Account)
def my_callback(sender, instance, *args, **kwargs):
    status, msg = send_registration_email(instance.email)
    print(status, msg)
