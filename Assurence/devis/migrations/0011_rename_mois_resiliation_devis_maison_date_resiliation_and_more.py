# Generated by Django 4.0.2 on 2022-02-21 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0010_remove_devis_maison_nbr_resiliation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devis_maison',
            old_name='mois_resiliation',
            new_name='date_resiliation',
        ),
        migrations.RemoveField(
            model_name='devis_maison',
            name='periode_prochaine_resiliation',
        ),
    ]
