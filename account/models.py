from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta


class User(AbstractUser):
    is_verified = models.BooleanField(default=False)
    token_created_date = models.DateTimeField(default=timezone.now)
    verified_date = models.DateTimeField(null=True, blank=True)
    token = models.CharField(max_length=1024, null=True, blank=True)

    @property
    def is_token_expired(self):
        if self.token_created_date + timedelta(days=2) < timezone.now():
            # Token ishlamidi
            return True
        return False
