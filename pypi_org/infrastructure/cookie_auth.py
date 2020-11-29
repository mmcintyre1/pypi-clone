from datetime import timedelta
from flask import Request
from flask import Response
import hashlib
from typing import Optional

from pypi_org.bin.load_data import try_int


AUTH_COOKIE_NAME = 'pypi_demo_user'


def set_auth(response: Response, user_id: int):
    hash_val = __hash_text(str(user_id))
    val = f"{user_id}:{hash_val}"
    response.set_cookie(AUTH_COOKIE_NAME, val)


def __hash_text(text: str) -> str:
    text = f'salty__{text}__text'
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def __add_cookie_callback(_, response: Response, name: str, value: str):
    response.set_cookie(name, value, max_age=timedelta(days=30))


def get_user_id_via_auth_cookie(request: Request) -> Optional[int]:
    if AUTH_COOKIE_NAME not in request.cookies:
        return None

    val = request.cookies[AUTH_COOKIE_NAME]
    parts = val.split(':')
    if len(parts) != 2:
        return None

    user_id = parts[0]
    hash_val = parts[1]
    hash_val_check = __hash_text(user_id)

    if hash_val != hash_val_check:
        print('Warning: Hash Mismatch, invalid cookie value!')
        return None

    return try_int(user_id)


def logout(response: Response):
    response.delete_cookie(AUTH_COOKIE_NAME)