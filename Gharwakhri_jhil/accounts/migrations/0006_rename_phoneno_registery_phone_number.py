# Generated by Django 4.1.7 on 2023-03-16 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_registery_terms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registery',
            old_name='phoneno',
            new_name='phone_number',
        ),
    ]
