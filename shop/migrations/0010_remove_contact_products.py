# Generated by Django 5.0.4 on 2024-04-21 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_contact_comments_contact_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='products',
        ),
    ]
