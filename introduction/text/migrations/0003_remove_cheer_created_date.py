# Generated by Django 3.0.5 on 2020-05-12 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0002_cheer_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cheer',
            name='created_date',
        ),
    ]