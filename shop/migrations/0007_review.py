# Generated by Django 5.0.4 on 2024-04-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_contact_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
