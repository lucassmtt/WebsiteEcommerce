from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class User(User):
    oid = models.UUIDField(
        db_column='oid_user',
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )
    
    name = models.CharField(
        max_length=255,
        null=False,
        blank=True
    )
    
    email = models.EmailField(
        max_length=255,
        null=False,
        blank=True,
        unique=True
    )
    
    phone = models.CharField(
        max_length=11,
        null=False,
        blank=True,
        unique=True,
    )
    
    cpf = models.CharField(
        max_length=11,
        null=False,
        blank=True,
        unique=True,
    )
    
    password = models.TextField(
        max_length=255,
        null=False,
    )
    
    def __str__(self) -> str:
        return self.name, self.email, self.phone, self.cpf
  