# Generated by Django 4.0.2 on 2022-02-04 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prospect', '0001_initial'),
        ('devis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devis',
            name='prospect',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prospect.prospect'),
        ),
    ]
