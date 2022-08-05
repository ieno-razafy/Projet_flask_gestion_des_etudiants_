# Projet_flask_gestion_des_etudiants_
Projet_ lask gestion des etudiants

INFORMATION
*****************************************************************************
ENVIRONEMENT DE DEVELOPPEMENT
Linux(Ubuntu20.04)
mongodb 5.0.6
Python 3.8.10
*****************************************************************************
CREER UN ENVIRONEMENT VIRTUEL TOUT EN INSTALLANT LES PAQUETS SUIVANTS:
Package           Version
----------------- -------
Flask==2.2.1
flask-mongoengine==1.0.0

*****************************************************************************
INFORMATION SUR LA BASE DE DONNEES

les base de donnees se trouvent dans le repertoire: 0__base_de_donnees

db_name = "db"
collections: 1.etudiant_collection {"photo","nom", "prenom","cycle","mention" }
             2.autentification {"username", "pswd"}

*****************************************************************************
projet/
├── 0__base_de_donnees
│   ├── autentification.json
│   └── etudiant_collection.json
├── etudiantApp
│   ├── __init__.py
│   ├── __pycache__
│   ├── static
│   ├── templates
│   └── views.py
├── env
│   ├── bin
│   ├── include
│   ├── lib
│   ├── lib64 -> lib
│   ├── pyvenv.cfg
│   └── share
├── readme.md
└── run.py

11 directories, 7 files
EXECUTION DE L'APPLICATION
1.etape: entrer dans la repertoire fac_science
2. executer la commande suivantes: - Linux(OS) : python3 run.py
                                   - Windows(OS): py run.py

*****************************************************************************
AUTENTIFICATION:
Utilisateur: papasi
mot_de_passe: papasi4

*****************************************************************************
BIENVENUE ALORS AU MICRO-APPLICATION: GESTION DES ETUDIANTS (CRUD)
*****************************************************************************
Faiblesse de l'Application: Le system de gestion des sessions n'est pas encore prise en charge!
