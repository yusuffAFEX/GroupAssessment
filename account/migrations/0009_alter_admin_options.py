# Generated by Django 4.1 on 2022-08-31 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_userprofile_is_admin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'permissions': (('admin', 'Can remove and add people'),)},
        ),
    ]
