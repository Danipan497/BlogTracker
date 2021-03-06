# Generated by Django 3.1.5 on 2021-01-21 09:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('new_sites', '0008_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name_plural': 'projects'},
        ),
        migrations.AddField(
            model_name='project',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
