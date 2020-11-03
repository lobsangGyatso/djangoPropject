# Generated by Django 2.2.2 on 2019-08-09 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoAuthentication', '0029_auto_20190809_0838'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='coursemanagement',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='OfferedCourses',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('session', models.CharField(max_length=4)),
                ('courseCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoAuthentication.CourseManagement')),
            ],
        ),
        migrations.RemoveField(
            model_name='coursemanagement',
            name='session',
        ),
        migrations.RemoveField(
            model_name='coursemanagement',
            name='year',
        ),
    ]