# Generated by Django 4.0.2 on 2022-02-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0003_remove_devis_type_propriete_devis_garanties_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devis',
            name='type_proprietide',
        ),
        migrations.AddField(
            model_name='devis',
            name='type_propriete',
            field=models.CharField(blank=True, choices=[('Locataire', 'Locataire')], max_length=20, null=True, verbose_name='Type_propriete'),
        ),
    ]
