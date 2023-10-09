from django.db import models
import uuid

# Create your models here.
class Category(models.Model):
    oid = models.UUIDField(
        db_column='oid_category',
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
    
    description = models.CharField(
        max_length=255,
        null=False,
        blank=True
    )
    
    def __str__(self) -> str:
        return f'Name: {self.name} Description: {self.description}'
    
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
