# Generated by Django 2.2.1 on 2019-08-06 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0023_auto_20190805_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='password',
        ),
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
        migrations.RemoveField(
            model_name='order',
            name='username',
        ),
        migrations.RemoveField(
            model_name='order',
            name='zipcode',
        ),
    ]