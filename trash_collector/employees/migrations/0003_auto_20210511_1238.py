# Generated by Django 3.1.8 on 2021-05-11 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20210511_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='pickup_day',
            field=models.DateField(default=None, verbose_name=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']),
        ),
        migrations.AlterField(
            model_name='employee',
            name='zipcode',
            field=models.IntegerField(default=None, max_length=5),
        ),
    ]
