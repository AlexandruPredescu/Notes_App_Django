# Generated by Django 4.2.9 on 2024-02-02 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_note_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='owner',
        ),
    ]
