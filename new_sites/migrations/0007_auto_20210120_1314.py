# Generated by Django 3.1.5 on 2021-01-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_sites', '0006_auto_20210120_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='short',
            field=models.CharField(default='default string', max_length=100),
        ),
    ]
