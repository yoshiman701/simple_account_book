# Generated by Django 3.2.4 on 2021-09-15 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_calendar', '0002_money_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='money',
            name='date',
        ),
        migrations.RemoveField(
            model_name='money',
            name='serial',
        ),
    ]