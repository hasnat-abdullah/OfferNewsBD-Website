# Generated by Django 2.1.2 on 2019-02-07 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offernewsapp', '0010_auto_20190129_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='expiredOn',
            field=models.DateField(),
        ),
    ]
