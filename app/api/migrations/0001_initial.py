# Generated by Django 4.2.6 on 2023-10-07 21:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('oid', models.UUIDField(blank=True, db_column='oid_category', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.UUIDField(blank=True, db_column='oid_order', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('totalPrice', models.FloatField(null=True)),
                ('status', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('oid', models.UUIDField(blank=True, db_column='oid_user', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255, unique=True)),
                ('phone', models.CharField(blank=True, max_length=11, unique=True)),
                ('cpf', models.CharField(blank=True, max_length=11, unique=True)),
                ('password', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('oid', models.UUIDField(blank=True, db_column='oid_product', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.UUIDField(blank=True)),
                ('price', models.FloatField(max_length=10, null=True)),
                ('description', models.TextField(max_length=255, null=True)),
                ('lenght', models.SmallIntegerField(max_length=3)),
                ('category_oid', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
            options={
                'verbose_name': 'produto',
                'verbose_name_plural': 'produtos',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('oid', models.UUIDField(blank=True, db_column='oid_orderItem', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('order_oid', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.order')),
                ('product_oid', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user_oid',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]
