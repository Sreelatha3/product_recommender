# Generated by Django 4.2.20 on 2025-04-30 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(related_name='orders', to='products.product')),
            ],
        ),
    ]
