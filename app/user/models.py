from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class User(models.Model):
    oid = models.UUIDField(
        db_column='oid_user',
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )
    
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    
    phone = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        unique=True,
    )
    
    cpf = models.CharField(
        max_length=11,
        null=True,
        unique=True,
    )
    
    image = models.ImageField()


    def __str__(self) -> str:
        return self.name, self.email, self.phone, self.cpf
  