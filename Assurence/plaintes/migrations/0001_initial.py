# Generated by Django 4.0.2 on 2022-02-28 08:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plaintes',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sujet', models.CharField(blank=True, max_length=255, null=True, verbose_name='le sujet de la plainte')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email de client qui pose le question')),
                ('answer', models.TextField(blank=True, max_length=1000, null=True)),
                ('date_ajout', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
            ],
        ),
    ]
