# Generated by Django 3.1.5 on 2021-01-22 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_sites', '0025_auto_20210122_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectentry',
            name='image',
            field=models.FileField(upload_to='media/'),
        ),
    ]
