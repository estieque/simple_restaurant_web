# Generated by Django 4.1 on 2022-08-24 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_alter_reservation_date_alter_reservation_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='content',
            new_name='message',
        ),
    ]