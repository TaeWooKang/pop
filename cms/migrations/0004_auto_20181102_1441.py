# Generated by Django 2.1.2 on 2018-11-02 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20181102_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='data',
            new_name='date',
        ),
    ]
