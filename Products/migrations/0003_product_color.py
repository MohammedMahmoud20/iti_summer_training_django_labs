# Generated by Django 4.2.5 on 2023-09-28 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='black', max_length=10),
        ),
    ]