# Generated by Django 3.2.9 on 2021-12-08 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0005_crawlingqueue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawlingqueue',
            name='url',
            field=models.TextField(),
        ),
    ]
