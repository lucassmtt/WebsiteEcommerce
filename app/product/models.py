from category.models import Category
from django.db import models
import uuid


class Product(models.Model):
    oid = models.UUIDField(
        db_column='oid_product',
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )
    
    name = models.UUIDField(
        max_length=255,
        null=False,
        blank=True
    )
    
    price = models.FloatField(
        null=True,
        max_length=10,   
    )
    
    description = models.TextField(
        max_length=255,
        null=True,
    )
    
    lenght = models.SmallIntegerField(
    )
    
    category_oid = models.ForeignKey(
        Category,
        blank=True,
        on_delete=models.CASCADE
    )
    
    similar_orders = models.TextField(
        max_length=255,
        null = true,
    )
    
    def __str__(self) -> str:
        return self.name, self.price, self.description, self.lenght, self.category_oid
    
    
    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'   
