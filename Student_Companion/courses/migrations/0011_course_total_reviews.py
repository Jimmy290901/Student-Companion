# Generated by Django 3.2.5 on 2021-08-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20210819_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='total_reviews',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
