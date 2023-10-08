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
    
    def __str__(self) -> str:
        return self.name, self.price, self.description, self.lenght, self.category_oid
    
    
    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'   
    
    
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
    
    
class Order(models.Model):
    oid = models.UUIDField(
        db_column='oid_order',
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )
    
    user_oid = models.ForeignKey(
        User,
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
    
    
class OrderItem(models.Model):
    oid = models.UUIDField(
        db_column='oid_orderItem',
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )
    
    order_oid = models.ForeignKey(
        Order,
        blank=True,
        on_delete=models.CASCADE
    )
    
    product_oid = models.ForeignKey(
        Product,
        blank=True,
        on_delete=models.CASCADE
    )
    
    quantity = models.IntegerField()
    
    def __str__(self) -> str:
        return self.oid, self.order_oid, self.product_oid, self.quantity