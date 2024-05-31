from django.contrib.auth.models import AbstractUser
from django.db import models
import random

def generate_confirmation_code():
    return ''.join(random.choices('0123456789', k=6))

class User(AbstractUser):
    is_active = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=6, default=generate_confirmation_code)