# Generated by Django 3.1.3 on 2021-02-03 19:30

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210203_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='index.PNG', null=True, upload_to=posts.models.upload_location),
        ),
    ]
