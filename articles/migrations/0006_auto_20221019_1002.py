# Generated by Django 3.1.14 on 2022-10-19 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_subscribedusers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribedusers',
            name='message',
        ),
        migrations.RemoveField(
            model_name='subscribedusers',
            name='name',
        ),
    ]
