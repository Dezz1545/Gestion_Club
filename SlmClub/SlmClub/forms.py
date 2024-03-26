from django import forms
from Entite.models import Quittance, Commune, Category, Menbre




class QuittanceForm(forms.ModelForm):
    class Meta:
        model = Quittance
        fields = ['nom_quittance', 'libelle_quittance', 'date_quittance']
        widgets = {
            'nom_quittance': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Nom de la quittance'}),
            'libelle_quittance': forms.Textarea(attrs={'rows': 4, 'class': 'form-control mb-3', 'placeholder': 'Libellé de la quittance'}),  
            'date_quittance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-3', 'placeholder': 'Date de la quittance'})  
        }

class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = ['nom_commune', 'description_commune', 'nom_maire', 'etoile_commune']
        widgets = {
            'description_commune': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'})  
        }
        


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['designation', 'description', 'cotisation']

class MenbreForm(forms.ModelForm):
    class Meta:
        model = Menbre
        fields = ['nom', 'prenom', 'sexe', 'commune', 'category']



    


