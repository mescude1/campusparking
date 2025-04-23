from UserProfile import create_app
from UserProfile.models.user_model import db, User

app = create_app()

with app.app_context():  # ✅ Contexto de la app
    new_user = User(name="Juan Pérez", email="juan@example.com", role="cliente", phone="123456789")
    db.session.add(new_user)
    db.session.commit()

    print("Usuario creado con ID:", new_user.id)