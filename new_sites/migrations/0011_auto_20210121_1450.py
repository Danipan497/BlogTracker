# Generated by Django 3.1.5 on 2021-01-21 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_sites', '0010_auto_20210121_1209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectentry',
            options={'verbose_name_plural': 'projectentries'},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='projectentry',
            old_name='description',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='projectentry',
            name='technology',
        ),
    ]