from django.core.validators import MinValueValidator
from django.db import models
import uuid


# Create your models here.


class Prospect(models.Model):
    id = models.CharField(default=uuid.uuid4,  unique=True, primary_key=True, max_length=20, editable=False)
    nom = models.CharField(verbose_name="Prénom", max_length=30, blank=True, null=True)
    prenom = models.CharField(verbose_name="Nom", max_length=30, blank=True, null=True)
    adresse_email = models.EmailField(verbose_name="Email", blank=True, null=True)
    adress = models.CharField(max_length=255, blank=True, null=True)
    date_naissance  =  models.CharField(max_length=55 ,  null=True , blank=True)
    add_date = models.DateField(verbose_name="Date d'ajout", auto_now_add=True)
    reminded = models.IntegerField(verbose_name="remided times", blank=True, null=True,
                                   validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return str(self.id) + " " + self.nom + " " + self.prenom
