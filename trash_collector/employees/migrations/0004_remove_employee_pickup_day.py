# Generated by Django 3.1.8 on 2021-05-11 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20210511_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='pickup_day',
        ),
    ]
