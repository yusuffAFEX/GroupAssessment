# Generated by Django 4.1 on 2022-08-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_userprofile_options_alter_userprofile_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_member',
            field=models.BooleanField(default=False),
        ),
    ]