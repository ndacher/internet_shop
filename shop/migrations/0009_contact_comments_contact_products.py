# Generated by Django 5.0.4 on 2024-04-21 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='products',
            field=models.ManyToManyField(to='shop.product'),
        ),
    ]