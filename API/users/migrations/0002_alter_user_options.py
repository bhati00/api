# Generated by Django 5.0.4 on 2024-04-22 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['created_at']},
        ),
    ]
