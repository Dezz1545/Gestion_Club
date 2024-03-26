from django.db import models

# Create your models here.




class Quittance(models.Model):
    nom_quittance = models.CharField(max_length=100)
    libelle_quittance = models.TextField()
    date_quittance = models.DateField()

    def __str__(self):
        return self.nom_quittance
 
class Commune(models.Model):
    nom_commune = models.CharField(max_length=100)
    description_commune = models.TextField()
    nom_maire = models.CharField(max_length=100)
    etoile_commune = models.IntegerField(default=0)  # Nombre d'étoiles de la commune

    def __str__(self):
        return self.nom_commune
    
class Category(models.Model):
    designation = models.CharField(max_length=100)
    description = models.TextField()
    cotisation = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.designation
    
class Menbre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('Autre', 'Autre'),
    ]
    sexe = models.CharField(max_length=10, choices=SEXE_CHOICES)
    commune = models.ForeignKey('Commune', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
