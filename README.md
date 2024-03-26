Pour faire fonctionner un projet Django, suivez ces étapes :

Installation de Django et Pillow
Installer Django :

Assurez-vous d'avoir Python installé sur votre système. Vous pouvez le télécharger depuis le site officiel de Python : https://www.python.org/downloads/
Une fois Python installé, ouvrez votre terminal et utilisez pip, le gestionnaire de packages de Python, pour installer Django :

pip install django
Installer Pillow :

Pillow est une bibliothèque Python requise pour le traitement d'images dans Django. Vous pouvez l'installer en utilisant pip également :

pip install pillow
Faire fonctionner votre projet Django
Cloner votre projet (s'il n'est pas déjà sur votre machine) :

Si vous avez déjà un projet Django, assurez-vous de le cloner sur votre machine. Si vous n'avez pas encore un projet, créez-en un avec la commande suivante :

django-admin startproject nom_de_votre_projet
Naviguer dans le répertoire de votre projet :



cd nom_de_votre_projet
Effectuer les migrations de la base de données :

Django utilise des migrations pour gérer les changements de schéma de base de données. Exécutez les migrations pour créer la structure initiale de votre base de données :

python manage.py migrate
Créer un superutilisateur (optionnel) :

Si vous souhaitez avoir accès à l'interface d'administration de Django, vous pouvez créer un superutilisateur :

python manage.py createsuperuser
Suivez les instructions pour créer le superutilisateur.
Lancer le serveur de développement :

Pour exécuter votre projet Django localement, utilisez la commande :

python manage.py runserver
Cela lancera un serveur de développement sur votre machine. Vous pouvez accéder à votre projet en ouvrant un navigateur web et en visitant l'adresse http://localhost:8000/.
Accéder à l'interface d'administration :

Si vous avez créé un superutilisateur, vous pouvez accéder à l'interface d'administration de Django en visitant http://localhost:8000/admin/ dans votre navigateur. Connectez-vous avec les informations d'identification du superutilisateur que vous avez créé.
C'est tout ! Vous devriez maintenant avoir votre projet Django fonctionnant sur votre machine locale. N'oubliez pas de consulter la documentation officielle de Django pour plus d'informations sur la création et le déploiement de projets Django : https://docs.djangoproject.com/en/stable/
