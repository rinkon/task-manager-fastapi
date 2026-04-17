from datetime import datetime, timedelta
from jose import jwt
from app.core import config


def create_token(data: dict):
    life_time = datetime.utcnow() + timedelta(minutes=config.TOKEN_LIFETIME_IN_MINUTES)
    data.update({'exp': life_time})

    return jwt.encode(data, config.SECRET_KEY, config.ALGORITHM)
