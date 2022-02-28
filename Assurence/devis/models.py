from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from prospect.models import Prospect
from multiselectfield import MultiSelectField


# Create your models here.


class Devis_Maison(models.Model):
    Categories = (('item_key1', 'Item title 1.1'),
                  ('item_key2', 'Item title 1.2'),
                  ('item_key3', 'Item title 1.3'),
                  ('item_key4', 'Item title 1.4'),
                  ('item_key5', 'Item title 1.5'))
    Type_propriete = (("Locataire", "Locataire"),
                      ("proprietaire", "proprietaire"),
                      ("proprietaire non occupant", "proprietaire non occupant"))
    Type_residence = (("principale", "principale"),
                      ("secondaire", "secondaire"))
    nombre_sinistre = (("Aucun", "Aucun"), ("un", "un"), ("deux", "deux"), ("Trois ou plus", "Trois ou plus"))
    Type_resiliation = (("demenage", "demenage"), ("changer habitat", "changer habitat"))
    periode_res = (("plus de 12 mois ", "plus de 12 mois"), ("Moin de 12 mois", "Moin de 12 mois"))
    surface_depandance_choix = (("plus de 100 m ", "plus de 100 m"), ("Moin de 21 m", "Moin de 21 m"),
                                ("entre 21 m et 100 m ", "entre 21 m et 100 m"))
    periode_construction = (("Avant 1960", "Avant 1960"), ("Entre 1960 et 1980", "Entre 1960 et 1980"),
                            ("Entre 1981 et 2000 ", "Entre 1981 et 2000"), ("Après 2001", "Après 2001"))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=True, editable=False, max_length=20)
    prospect = models.OneToOneField(Prospect, verbose_name="le proprietary de devis", blank=True, null=True,
                                    on_delete=models.CASCADE)
    email_prospect = models.EmailField(verbose_name="email de prospect", blank=True, null=True)
    Vérnada = models.BooleanField(verbose_name="est ce il y a veranda", default=False)
    Cheminée = models.BooleanField(verbose_name="est ce il y a Cheminée", default=False)
    Piscine = models.BooleanField(verbose_name="est ce il y a Piscine", default=False)
    besoin_resiliation = models.BooleanField(verbose_name="avez vous ancien assurence", default=False)
    type_residence = models.CharField(verbose_name="Type_residence", max_length=255, blank=True, null=True,
                                      choices=Type_residence)
    type_propriete = models.CharField(verbose_name="Type_propriete", max_length=255, blank=True, null=True,
                                      choices=Type_propriete)
    interraction = models.BooleanField(verbose_name="permission de contrat", blank=True, null=True)
    Surface = models.IntegerField(verbose_name="surface habitat", blank=True, null=True,
                                  validators=[MinValueValidator(25), MaxValueValidator(1000)], default=25)
    nbrChambre = models.IntegerField(verbose_name="Nombre des Chambres", blank=True,
                                     validators=[MinValueValidator(0), MaxValueValidator(25)], default=0, null=True)
    dependance = models.BooleanField(verbose_name="depandance de residance", blank=True, null=True, default=False)
    surface_depandance = models.CharField(verbose_name="surface de depandance", max_length=255, blank=True, null=True,
                                          default=0, choices=surface_depandance_choix)
    periode_construction = models.CharField(verbose_name="annee de contruction de maison", max_length=80, blank=True,
                                            null=True, choices=periode_construction)
    garanties = MultiSelectField(choices=Categories, blank=True, null=True)
    type_resiliation = models.CharField(verbose_name="type de resiliation", max_length=255, blank=True, null=True,
                                        choices=Type_resiliation)
    nbr_sinistre = models.CharField(verbose_name="nombre des sinistre", max_length=255, blank=True, null=True,
                                    choices=nombre_sinistre)
    resiliation = models.BooleanField(verbose_name="Besoin resiliation", blank=True, null=True)
    periode_resiliation = models.CharField(verbose_name="periode de resiliation", max_length=255, blank=True, null=True,
                                           choices=periode_res)
    date_resiliation = models.CharField(verbose_name="mois de resiliation", max_length=15, blank=True, null=True)
    Tarification = models.FloatField(verbose_name="Tarification devis", blank=True, null=True)
    franchise = models.FloatField(verbose_name="Franchise sur devis", blank=True, null=True)

    def __str__(self):
        return "Devis Maison"


class Devis_Appartement(models.Model):
    Categories = (('item_key1', 'Item title 1.1'),
                  ('item_key2', 'Item title 1.2'),
                  ('item_key3', 'Item title 1.3'),
                  ('item_key4', 'Item title 1.4'),
                  ('item_key5', 'Item title 1.5'))
    Type_propriete = (("Locataire", "Locataire"),
                      ("proprietaire", "proprietaire"),
                      ("proprietaire non occupant", "proprietaire non occupant"))
    Type_residence = (("principale", "principale"),
                      ("secondaire", "secondaire"))
    nombre_resiliation = (("Aucun", "Aucun"), ("un", "un"), ("deux", "deux"), ("Trois ou plus", "Trois ou plus"))
    Type_resiliation = (("demenage", "demenage"), ("changer habitat", "changer habitat"))
    periode_res = (("plus de 12 mois ", "plus de 12 mois"), ("Moin de 12 mois", "Moin de 12 mois"))
    surface_depandance_choix = (("plus de 100 m ", "plus de 100 m"), ("Moin de 21 m", "Moin de 21 m"),
                                ("entre 21 m et 100 m ", "entre 21 m et 100 m"))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=True, editable=False, max_length=20)

    prospect = models.OneToOneField(Prospect, verbose_name="le proprietary de devis", blank=True, null=True,
                                    on_delete=models.CASCADE)
    email_prospect = models.EmailField(verbose_name="email de prospect", blank=True, null=True)
    ancien_assurence = models.BooleanField(verbose_name="avez vous ancien assurence", default=False)
    type_residence = models.CharField(verbose_name="Type_residence", max_length=255, blank=True, null=True,
                                      choices=Type_residence)
    type_propriete = models.CharField(verbose_name="Type_propriete", max_length=255, blank=True, null=True,
                                      choices=Type_propriete)
    interraction = models.BooleanField(verbose_name="permission de contrat", blank=True, null=True)
    Surface = models.IntegerField(verbose_name="surface habitat", blank=True, null=True,
                                  validators=[MinValueValidator(25), MaxValueValidator(1000)], default=25)
    nbrChambre = models.IntegerField(verbose_name="Nombre des Chambres", blank=True,
                                     validators=[MinValueValidator(0), MaxValueValidator(25)], default=0, null=True)
    dependance = models.BooleanField(verbose_name="depandance de residance", blank=True, null=True, default=False)
    surface_depandance = models.CharField(verbose_name="surface de depandance", max_length=255, blank=True, null=True,
                                          default=0, choices=surface_depandance_choix)
    garanties = MultiSelectField(choices=Categories, blank=True, null=True)
    type_resiliation = models.CharField(verbose_name="type de resiliation", max_length=255, blank=True, null=True,
                                        choices=Type_resiliation)
    nbr_resiliation = models.CharField(verbose_name="nombre des resiliation", max_length=255, blank=True, null=True,
                                       choices=nombre_resiliation)
    resiliation = models.BooleanField(verbose_name="Besoin resiliation", blank=True, null=True)
    periode_resiliation = models.CharField(verbose_name="periode de resiliation", max_length=255, blank=True, null=True,
                                           choices=periode_res)
    mois_resiliation = models.CharField(verbose_name="mois de resiliation", max_length=15, blank=True, null=True)
    periode_prochaine_resiliation = models.DateField(verbose_name="date de prochaine resiliation", null=True,
                                                     blank=True)
    Tarification = models.FloatField(verbose_name="Tarification devis", blank=True, null=True)
    franchise = models.FloatField(verbose_name="Franchise sur devis", blank=True, null=True)

    def __str__(self):
        return "Devis Appartement" + str(self.id)


class Devis_Immeuble(models.Model):
    Categories = (('item_key1', 'Item title 1.1'),
                  ('item_key2', 'Item title 1.2'),
                  ('item_key3', 'Item title 1.3'),
                  ('item_key4', 'Item title 1.4'),
                  ('item_key5', 'Item title 1.5'))
    niveau_immeuble = (('5 niveau ou plus ', '5 niveau ou plus '),
                       ('Entre 6 et 8 niveaux', 'Entre 6 et 8 niveaux'),
                       ('9 niveaux ou plus', '9 niveaux ou plus'))
    niveau_sous_sol = (('Aucun ', 'Aucun'),
                       ('Moins de 3 Niveaux', 'Moins de 3 Niveaux'),
                       ('3 niveauc ou plus', '3 niveauc ou plus'))
    Type_propriete = (("coproprieté", "coproprieté"),
                      ("monoproprieté", ""),
                      ("HLM", "HLM"))
    choix_parking = (("Pad de parking", "Pad de parking"), ("Place de parking", "Place de parking"),
                     ("Place de parking et box", "Place de parking et box"), ("Box fermé", "Box fermé"))
    Type_copropriete = (("verticale", "verticale"),
                        ("horizontal", "horizontal"))
    Type_batiment = (("Standard", "Standard"),
                     ("Standing", "Standing"))
    periode_construction = (("Avant 1960", "Avant 1960"), ("Entre 1960 et 1980", "Entre 1960 et 1980"),
                            ("Entre 1981 et 2000 ", "Entre 1981 et 2000"), ("Après 2001", "Après 2001"))
    Installation = (("Aucun", "Aucun"),
                    ("Réseau de sitribution de gaz", "Réseau de sitribution de gaz"),
                    ("Rien à signaler", "Rien à signaler"))
    Traveaux = (("Toiture", "Toiture"),
                ("Plombier", "Plombier"),
                ("Facade", "Facade"))

    Usage = (("Habitaion", "Habitaion"),
             ("Activité commerciale ou professionnel", "Activité commerciale ou professionnel"))

    choix_occupation = (("Occupé pour plus de 75% de sa surface ", "Occupé pour plus de 75% de sa surface "),
                        ("Occupé entre 50% et 75% de sa surface ", "Occupé entre 50% et 75% de sa surface "),
                        ("Occupé pour moins de 50% de sa surface", "Occupé pour moins de 50% de sa surface"),
                        ("Non, inoccupé et/ou arreté de péril ", "Non, inoccupé et/ou arreté de péril "))
    nombre_sinistre = (("Aucun", "Aucun"), ("un", "un"), ("deux", "deux"), ("Trois ou plus", "Trois ou plus"))
    Type_entreprise = (
        ("Un particulier ", "Un particulier "), ("Une SCI", "Une SCI"), ("Une ASL / une AFULL", "Une ASL / une AFULL"),
        ("Un syndic bénévole", "Un syndic bénévole"),
        ("Un syndic professionnel", "Un syndic professionnel"),
        ("un membre du conseil syndical", "un membre du conseil syndical"),
        ("Une SAS / une SARL ", "Une SAS / une SARL "))
    Type_residence = (("principale", "principale"),
                      ("secondaire", "secondaire"))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=True, editable=False, max_length=20)
    Surface = models.IntegerField(verbose_name="surface habitat", blank=True, null=True,
                                  validators=[MinValueValidator(25), MaxValueValidator(1000)], default=25)

    nombre_lots = models.IntegerField(verbose_name="Nombre de lots", blank=True,
                                      validators=[MinValueValidator(0), MaxValueValidator(25)], default=0, null=True)
    Niveau_immeuble = models.CharField(verbose_name="niveau d'etage de l immeuble ", max_length=255, blank=True,
                                       null=True,
                                       choices=niveau_immeuble)
    Niveau_sous_sol = models.CharField(verbose_name="niveau sous sol de l immeuble ", max_length=255, blank=True,
                                       null=True,
                                       choices=niveau_sous_sol)
    Parking = models.CharField(verbose_name="Type de parking", max_length=255, blank=True,
                               null=True,
                               choices=choix_parking)
    type_propriete = models.CharField(verbose_name="Type_propriete", max_length=255, blank=True, null=True,
                                      choices=Type_propriete)
    type_copropriete = models.CharField(verbose_name="Type_copropriete", max_length=255, blank=True, null=True,
                                        choices=Type_copropriete)
    type_batiment = models.CharField(verbose_name="Type_copropriete", max_length=255, blank=True, null=True,
                                     choices=Type_batiment)
    periode_construction = models.CharField(verbose_name="annee de contruction de l'immeuble", max_length=80,
                                            blank=True,
                                            null=True, choices=periode_construction)
    installation = MultiSelectField(choices=Installation, verbose_name="installations", blank=True, null=True)
    traveaux = MultiSelectField(choices=Traveaux, verbose_name="Les Traveau réalisé", blank=True, null=True, )
    usage_immeuble = MultiSelectField(choices=Usage, blank=True, null=True,
                                      )

    activite_commerciale = models.CharField(max_length=355, blank=True, null=True)

    occupation = models.CharField(verbose_name="Taux d'ccupation", max_length=255, blank=True,
                                  null=True,
                                  choices=choix_occupation)

    taux_proprietaire = models.BooleanField(verbose_name="plus de 50% des proprietaire sont occupant", blank=True,
                                            null=True)

    nbr_sinistre = models.CharField(verbose_name="nombre des sinistre", max_length=255, blank=True, null=True,
                                    choices=nombre_sinistre)
    type_entreprise = models.CharField(verbose_name="nombre des sinistre", max_length=255, blank=True, null=True,
                                       choices=Type_entreprise)

    prospect = models.OneToOneField(Prospect, verbose_name="le proprietary de devis", blank=True, null=True,
                                    on_delete=models.CASCADE)
    date_assemblee = models.DateField(verbose_name="la date de l'assemblé generale", null=True, blank=False)

    ancien_assurence = models.BooleanField(verbose_name="avez vous ancien assurence", default=False)

    resiliation = models.BooleanField(verbose_name="Besoin resiliation", blank=True, null=True)

    type_residence = models.CharField(verbose_name="Type_residence", max_length=255, blank=True, null=True,
                                      choices=Type_residence)
    surface_immeuble = models.BooleanField(max_length=255, verbose_name="Entre 1 et 25% de la surface de l'immeuble",
                                           default=True)

    periode_prochaine_resiliation = models.DateField(verbose_name="date de prochaine resiliation", null=True,
                                                     blank=True)
    garanties = MultiSelectField(choices=Categories, blank=True, null=True)
    Tarification = models.FloatField(verbose_name="Tarification devis", blank=True, null=True)
    franchise = models.FloatField(verbose_name="Franchise sur devis", blank=True, null=True)
    email_prospect = models.EmailField(verbose_name="email de prospect", blank=True, null=True)

    def __str__(self):
        return "Devis Immeuble" + str(self.id)
