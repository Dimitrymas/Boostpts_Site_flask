import hashlib
import requests
from pathlib import Path


def new_avatar(id):
    id = str(id)
    file_path = Path(rf"./sweater/static/avatars/{id}.png")
    print(file_path)
    avatar = requests.get(
        f'http://www.gravatar.com/avatar/{hashlib.md5(id.encode("utf-8")).hexdigest()}?s=150&r=g&d=retro')
    with open(file_path, "wb") as f:
        f.write(avatar.content)
        f.close()
    return file_path
