# Generated by Django 4.0.2 on 2022-02-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0007_devis_appartement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devis_maison',
            name='periode_construction',
            field=models.CharField(blank=True, choices=[('Avant 1960', 'Avant 1960'), ('Entre 1960 et 1980', 'Entre 1960 et 1980'), ('Entre 1981 et 2000 ', 'Entre 1981 et 2000'), ('Après 2001', 'Après 2001')], max_length=80, null=True, verbose_name='annee de contruction de maison'),
        ),
    ]