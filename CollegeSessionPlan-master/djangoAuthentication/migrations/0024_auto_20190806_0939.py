# Generated by Django 2.2.2 on 2019-08-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoAuthentication', '0023_auto_20190806_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statustable',
            name='session',
            field=models.CharField(max_length=299),
        ),
        migrations.AlterField(
            model_name='statustable',
            name='status',
            field=models.CharField(max_length=299),
        ),
    ]
