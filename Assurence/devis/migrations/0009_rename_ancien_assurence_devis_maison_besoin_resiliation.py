# Generated by Django 4.0.2 on 2022-02-21 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0008_alter_devis_maison_periode_construction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devis_maison',
            old_name='ancien_assurence',
            new_name='besoin_resiliation',
        ),
    ]
