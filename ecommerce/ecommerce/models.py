import uuid

from django.db import models


class Product(models.Model):
    oid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True,
        max_length=255,
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    length = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        app_label = 'ecommerce'


class Category(models.Model):
    oid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True,
        max_length=255,
    )
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'category'
        app_label = 'ecommerce'


class Order(models.Model):
    oid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True,
        max_length=255,
    )
    status = models.IntegerField()

    class Meta:
        db_table = 'order'
        app_label = 'ecommerce'


class OrderItem(models.Model):
    oid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True,
        max_length=255,
    )
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_item'
        app_label = 'ecommerce'


class User(models.Model):
    oid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True,
        max_length=255,
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'tb_user'
        app_label = 'ecommerce'
