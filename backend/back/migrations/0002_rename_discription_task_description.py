# Generated by Django 3.2.7 on 2021-09-24 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='discription',
            new_name='description',
        ),
    ]
