# Generated by Django 3.1.8 on 2021-05-10 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='pickup_day',
            field=models.DateField(verbose_name=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']),
        ),
    ]
