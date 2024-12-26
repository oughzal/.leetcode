#vérifier la version de git
git --verison
#vérifier la configuration de git
git config --list
#vérifier la configuration de git
git config --global --list
#vérifier la configuration de git
git config --system --list
#vérifier la configuration de git
git config --local --list
#configurer le nom de l'utilisateur
git config --global user.name "nom_utilisateur"
#configurer l'email de l'utilisateur
git config --global user.email "email_utilisateur"
#configurer l'éditeur de texte (vscode)
git config --global core.editor "code --wait"

#créer un dossier
mkdir git
#entrer dans le dossier
cd git
#initialiser un dépôt git
git init
#créer un fichier
touch index.html
#ajouter le fichier à l'index
git add index.html
#ajouter le fichier à l'index
git add .
#ajouter le fichier à l'index
git add --all
#ajouter le fichier à l'index
git add -A
#ajouter le fichier à l'index
git add -u
#ajouter le fichier à l'index
git add *
#ajouter le fichier à l'index
git add .
#ajouter le fichier à l'index
git add -A
#ajouter le fichier à l'index
git add -u
#vérfier le statut des fichiers
git status
