# Generated by Django 4.2.5 on 2023-09-28 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_product_created_at_product_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='catigory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
