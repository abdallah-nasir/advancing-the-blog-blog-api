# Generated by Django 3.1.3 on 2021-01-27 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210127_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='timestamp',
            field=models.DateField(auto_now=True),
        ),
    ]
