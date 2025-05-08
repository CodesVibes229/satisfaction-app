from app.database import SessionLocal

try:
    db = SessionLocal()
    print("✅ Connexion à la base réussie !")
except Exception as e:
    print("❌ Erreur de connexion :", e)
finally:
    db.close()
