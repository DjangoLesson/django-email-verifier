from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail as __send_mail
from config import settings


def send_mail(subject, message, emails=[], **kwargs):
    __send_mail(
        subject, message, settings.EMAIL_HOST_USER, emails, **kwargs
    )



def send_activation_token(user):
    token = default_token_generator.make_token(user)
    user.token = token
    user.save()
    send_mail(
        'Hisobingizni faollashtiring',
        f"http://localhost/account/token/{token}/",
        [user.email]
    )
