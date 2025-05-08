
```markdown
# 🏦 Satisfaction App - Enquête de satisfaction client pour banque

Une API FastAPI simple et sécurisée pour gérer des enquêtes de satisfaction client dans une structure bancaire.

## 🚀 Fonctionnalités

- Création, gestion et consultation des enquêtes de satisfaction
- Stockage sécurisé via PostgreSQL
- Architecture modulaire (FastAPI + SQLAlchemy)
- Variables d’environnement protégées avec `.env`
- Prêt pour déploiement Docker (à venir)

---

## 🛠️ Technologies utilisées

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

---

## 🧱 Structure du projet

```

satisfaction-app/
│
├── app/
│   ├── main.py               # Point d'entrée FastAPI
│   ├── database.py           # Connexion sécurisée à la DB
│   ├── models/               # Modèles SQLAlchemy
│   ├── routes/               # Endpoints FastAPI
│   └── schemas/              # Schémas Pydantic
│
├── .env                      # Variables d'environnement (non versionné)
├── requirements.txt          # Dépendances Python
└── README.md                 # Ce fichier

````

---

## ⚙️ Installation & Lancement

### 1. Cloner le dépôt

```bash
git clone https://github.com/CodesVibes229/satisfaction-app.git
cd satisfaction-app
````

### 2. Créer un environnement virtuel

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Créer un fichier `.env`

```ini
# .env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=satisfaction_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
```

### 5. Lancer le serveur

```bash
uvicorn app.main:app --reload
```

Visitez ensuite [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) pour accéder à la documentation interactive Swagger.

---

## ✅ À venir

* Authentification JWT
* Dashboard d’administration (frontend)
* Déploiement avec Docker et CI/CD

---

## 📄 Licence

Projet open-source sous licence MIT.

