import random
import string
from sqlalchemy.orm import Session
from app import models


def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits  # a-zA-Z0-9
    return ''.join(random.choices(chars, k=length))

def is_unique_short_code(db: Session, short_code):
    # print(type(models.URL))
    db_short_code = db.query(models.URL).filter(models.URL.short_url == short_code).first()
    if db_short_code:
        return False
    else:
        return True