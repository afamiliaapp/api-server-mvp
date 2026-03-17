from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token


# -------------------------
# REGISTER USER
# -------------------------

def create_user(db: Session, payload):

    user = User(
        email=payload.email,
        firstname=payload.firstname,
        surname=payload.surname,
        password_hash=hash_password(payload.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# -------------------------
# LOGIN USER
# -------------------------

def login_user(db: Session, email: str, password: str):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    token = create_access_token({"user_id": user.id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }