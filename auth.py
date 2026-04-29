import hashlib
import datetime
from services import sheets


def _hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def login(email: str, password: str) -> bool:
    try:
        rows = sheets.find_rows("users", "email", email)
        if not rows:
            return False
        return rows[0].get("password_hash") == _hash(password)
    except Exception:
        return False


def register(username: str, email: str, password: str) -> tuple[bool, str]:
    try:
        if sheets.find_rows("users", "email", email):
            return False, "An account with that email already exists."
        sheets.append_row("users", {
            "username": username,
            "email": email,
            "password_hash": _hash(password),
            "created_at": datetime.datetime.now().isoformat(),
        })
        return True, ""
    except Exception as e:
        return False, str(e)
