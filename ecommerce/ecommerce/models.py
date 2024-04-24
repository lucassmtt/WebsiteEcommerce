from django.db import models


class Product(models.Model):
    oid = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    length = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        app_label = 'ecommerce'
        db_table = 'product'


class Category(models.Model):
    oid = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        app_label = 'ecommerce'
        db_table = 'category'


class Order(models.Model):
    oid = models.CharField(max_length=255, primary_key=True)
    status = models.IntegerField()

    class Meta:
        app_label = 'ecommerce'
        db_table = 'order'


class OrderItem(models.Model):
    oid = models.CharField(max_length=255, primary_key=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'ecommerce'
        db_table = 'order_item'


class User(models.Model):
    oid = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    password = models.CharField(max_length=255)

    class Meta:
        app_label = 'ecommerce'
        db_table = 'tb_user'
