from environs import Env

env = Env()
env.read_env()

POSTGRES_URI = env.str('POSTGRES_URI')
SECRET_KEY = env.str('SECRET_KEY')
ALGORITHM = env.str('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = env.str('ACCESS_TOKEN_EXPIRE_MINUTES')

