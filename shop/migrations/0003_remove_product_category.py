# Generated by Django 5.0.4 on 2024-04-20 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_category_alter_product_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]