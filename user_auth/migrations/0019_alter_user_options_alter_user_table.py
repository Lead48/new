# Generated by Django 4.2.7 on 2024-02-11 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0018_user_email_verification_token_user_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelTable(
            name='user',
            table='auth_user',
        ),
    ]
