# Generated by Django 3.2.5 on 2021-08-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_photo',
            field=models.ImageField(blank=True, null=True, upload_to='Course'),
        ),
    ]
