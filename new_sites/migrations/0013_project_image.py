# Generated by Django 3.1.5 on 2021-01-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_sites', '0012_projectentry_technology'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FilePathField(default='', path='/new_sites/static/new_sites/images'),
            preserve_default=False,
        ),
    ]
