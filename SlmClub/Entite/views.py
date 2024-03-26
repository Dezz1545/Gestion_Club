from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from SlmClub.forms import QuittanceForm, CommuneForm,CategoryForm, MenbreForm
from .models import Quittance,Commune,Category, Menbre

def index(request):
    return render(request, "index.html")

def Parametre(request):
    return render(request, "Parametre.html")

def Contact(request):
    return render(request, "Contact.html")



def quittance_view(request):  # Renommez la vue pour éviter la confusion avec le modèle
    quittances = Quittance.objects.all()  # Utilisation correcte du gestionnaire de modèle
    return render(request, 'Quittance.html', {'quittances': quittances})



def commune_view(request):
    communes = Commune.objects.all()  # Utilisation correcte du gestionnaire de modèle
    return render(request, 'commune.html', {'communes': communes})

def Categorie_view(request):
    categorys = Category.objects.all()
    return render(request, "Categorie.html", {'categorys': categorys})

def Menbre_view(request):
    # Récupérer tous les objets Menbre avec leurs objets commune et category associés
    menbres = Menbre.objects.select_related('commune', 'category').all()
    
    # Passer les objets récupérés au template
    return render(request, "Menbre.html", {'menbres': menbres})




 # Quittance 
 # Quittance 
 # Quittance 
 
def create_quittance(request):
    if request.method == 'POST':
        form = QuittanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Quittance.html')  # Rediriger vers une page de succès après l'enregistrement de la quittance
    else:
        form = QuittanceForm()
    return render(request, 'create_Quittance.html', {'form': form})


def modify_quittance(request, quittance_id):
    quittance = get_object_or_404(Quittance, id=quittance_id)
    if request.method == 'POST':
        form = QuittanceForm(request.POST, instance=quittance)  # Pré-remplir le formulaire avec les données existantes
        if form.is_valid():
            form.save()
            return redirect('Quittance.html')  # Redirection vers la liste des quittances après modification
    else:
        form = QuittanceForm(instance=quittance)  # Pré-remplir le formulaire avec les données existantes
    return render(request, 'modify_quittance.html', {'form': form})



def delete_quittance(request, quittance_id):
    quittance = get_object_or_404(Quittance, id=quittance_id)
    if request.method == 'POST':
        # Code pour supprimer la quittance
        quittance.delete()
        return redirect('Quittance.html')  # Redirection vers la liste des quittances après suppression
    else:
        # Afficher la page de confirmation de suppression
        return render(request, 'delete_quittance.html', {'quittance': quittance})



 # Commune
 # Commune
 # Commune

def create_commune(request):
    if request.method == 'POST':
        form = CommuneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Commune.html')  # Rediriger vers une page de succès après l'enregistrement de la commune
    else:
        form = CommuneForm()
    return render(request, 'create_Commune.html', {'form': form})

def modify_commune(request, commune_id):
    commune = get_object_or_404(Commune, id=commune_id)
    if request.method == 'POST':
        form = CommuneForm(request.POST, instance=commune)
        if form.is_valid():
            form.save()
            return redirect('commune_view')  # Redirige vers la liste des communes après modification
    else:
        form = CommuneForm(instance=commune)
    return render(request, 'modify_commune.html', {'form': form, 'commune': commune})

def delete_commune(request, commune_id):
    commune = get_object_or_404(Commune, id=commune_id)
    if request.method == 'POST':
        commune.delete()
        return redirect('Commune.html')  # Redirige vers la liste des communes après suppression
    return render(request, 'delete_commune.html', {'commune': commune})


 # Categorie
 # Categorie
 # Categorie

def create_categorie(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Categorie.html')  # Rediriger vers une page de succès après l'enregistrement de la quittance
    else:
        form = CategoryForm()
    return render(request, 'create_Categorie.html', {'form': form})

def modify_categorie(request, categorie_id):
    categorie = get_object_or_404(Category, id=categorie_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=categorie)  # Pré-remplir le formulaire avec les données existantes
        if form.is_valid():
            form.save()
            return redirect('Categorie.html')  # Redirection vers la liste des catégories après modification
    else:
        form = CategoryForm(instance=categorie)  # Pré-remplir le formulaire avec les données existantes
    return render(request, 'modify_categorie.html', {'form': form})

def delete_categorie(request, categorie_id):
    categorie = get_object_or_404(Category, id=categorie_id)
    if request.method == 'POST':
        # Code pour supprimer la catégorie
        categorie.delete()
        return redirect('Categorie.html')  # Redirection vers la liste des catégories après suppression
    else:
        # Afficher la page de confirmation de suppression
        return render(request, 'delete_categorie.html', {'categorie': categorie})

 # Menbre
 # Menbre
 # Menbre

def create_menbre(request):
    if request.method == 'POST':
        form = MenbreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Menbre.html')  # Rediriger vers une page de succès après l'enregistrement de la quittance
    else:
        form = MenbreForm()
    return render(request, 'create_Menbre.html', {'form': form})

def modify_menbre(request, menbre_id):
    menbre = get_object_or_404(Menbre, id=menbre_id)
    if request.method == 'POST':
        form = MenbreForm(request.POST, instance=menbre)  # Pré-remplir le formulaire avec les données existantes
        if form.is_valid():
            form.save()
            return redirect('Menbre.html')  # Redirection vers la liste des membres après modification
    else:
        form = MenbreForm(instance=menbre)  # Pré-remplir le formulaire avec les données existantes
    return render(request, 'modify_menbre.html', {'form': form})

def delete_menbre(request, menbre_id):
    menbre = get_object_or_404(Menbre, id=menbre_id)
    if request.method == 'POST':
        # Code pour supprimer le membre
        menbre.delete()
        return redirect('Menbre.html')  # Redirection vers la liste des membres après suppression
    else:
        # Afficher la page de confirmation de suppression
        return render(request, 'delete_menbre.html', {'menbre': menbre})









