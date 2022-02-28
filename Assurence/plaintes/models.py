from django.db import models
import uuid
# Create your models here.



class Plaintes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=True, editable=False, max_length=20)
    sujet =  models.CharField(max_length=255 ,verbose_name="le sujet de la plainte",  null=True , blank=True)
    email =  models.EmailField(verbose_name="Email de client qui pose le question" ,  null=True ,  blank=True)
    answer = models.TextField(max_length=1000 ,   null=True ,  blank=True)
    date_ajout =  models.DateField(auto_now_add=True)
    date_update =  models.DateField(auto_now=True)
    def __str__(self):
        return "plaintes" + str(self.id) + self.sujet
