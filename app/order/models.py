from django.db import models
from user import models as md_users
import uuid

# Create your models here.
    
class Order(models.Model):
    oid = models.UUIDField(
        db_column='oid_order',
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )
    
    user_oid = models.ForeignKey(
        md_users.User,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )
    
    totalPrice = models.FloatField(
        null=True,
    )
    
    status = models.IntegerField(
        null=True
    )
    
    def __str__(self) -> str:
        return self.oid, self.user_oid, self.totalPrice, self.status


