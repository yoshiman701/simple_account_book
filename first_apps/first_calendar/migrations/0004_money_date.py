# Generated by Django 3.2.4 on 2021-09-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_calendar', '0003_auto_20210915_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='日付'),
        ),
    ]
