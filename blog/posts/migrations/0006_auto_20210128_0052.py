# Generated by Django 3.1.3 on 2021-01-27 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210128_0049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='timestamp',
            new_name='time',
        ),
    ]