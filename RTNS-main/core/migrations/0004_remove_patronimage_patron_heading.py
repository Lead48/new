# Generated by Django 4.2.7 on 2024-04-02 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_patronimage_patron_heading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patronimage',
            name='patron_heading',
        ),
    ]
