# Generated by Django 4.0.2 on 2022-02-17 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prospect', '0002_prospect_reminded_alter_prospect_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prospect',
            old_name='Habitat',
            new_name='adress',
        ),
    ]
