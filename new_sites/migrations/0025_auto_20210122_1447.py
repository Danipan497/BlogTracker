# Generated by Django 3.1.5 on 2021-01-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_sites', '0024_auto_20210122_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectentry',
            name='image',
            field=models.FilePathField(path='/img'),
        ),
    ]
