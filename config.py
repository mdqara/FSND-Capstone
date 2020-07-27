import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "IX*u0NYUltKRp8tHH1G^C8Vt0rXl"

    