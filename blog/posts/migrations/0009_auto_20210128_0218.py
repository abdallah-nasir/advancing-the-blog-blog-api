# Generated by Django 3.1.3 on 2021-01-28 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210128_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
    ]