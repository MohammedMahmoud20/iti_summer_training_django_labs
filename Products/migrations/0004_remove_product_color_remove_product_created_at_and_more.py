# Generated by Django 4.2.5 on 2023-09-28 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_product_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='in_stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='no_of_items',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
    ]
