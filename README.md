````markdown
# 📊 Satisfaction Survey API

Une mini application backend conçue avec **FastAPI** pour permettre la création, la gestion et l’analyse de questionnaires de satisfaction (ex. : banque, entreprise, etc.).

## 🚀 Fonctionnalités principales

- Création de questionnaires
- Enregistrement des réponses
- Récupération des données
- API REST avec documentation automatique (Swagger)

---

## 🧰 Stack technique

- **Langage** : Python 3.10+
- **Framework** : FastAPI
- **ORM** : SQLAlchemy
- **Base de données** : PostgreSQL (ou SQLite pour tests)
- **Documentation** : Swagger UI intégrée à FastAPI

---

## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/ton-utilisateur/satisfaction-app.git
cd satisfaction-app
````

### 2. Créer et activer un environnement virtuel

```bash
python -m venv env
source env/bin/activate  # ou .\env\Scripts\activate sur Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données

Modifier la variable `DATABASE_URL` dans `app/database.py` :

```python
DATABASE_URL = "postgresql://user:password@localhost/satisfaction_db"
```

Créer la base avec PostgreSQL :

```bash
createdb satisfaction_db
```

---

## ▶️ Lancer le serveur

```bash
uvicorn app.main:app --reload
```

L'application sera accessible à l’adresse :
👉 [http://localhost:8000](http://localhost:8000)

La documentation Swagger est disponible ici :
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📁 Arborescence du projet

```
satisfaction-app/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── routes/
│       └── survey.py
├── requirements.txt
└── README.md
```

---

## ✅ À faire / Roadmap

* [x] Création de sondages
* [ ] Ajout de réponses via API
* [ ] Authentification pour les administrateurs
* [ ] Visualisation des résultats
* [ ] Interface frontend (React/Vue)

---

## 👤 Auteur

* [Ton Nom / Pseudo GitHub](https://github.com/ton-utilisateur)

---

## 📝 Licence

Ce projet est sous licence MIT. Utilisation libre avec attribution.

