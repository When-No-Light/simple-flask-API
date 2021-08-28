from envparse import env


env.read_envfile()



class Config:
    SECURITY_REGISTERABLE = env.bool('SECURITY_REGISTERABLE')
    POSTGRES_USER = env('POSTGRES_USER', cast=str, default='localhost')
    POSTGRES_PASSWORD = env('POSTGRES_PASSWORD', cast=str)
    POSTGRES_HOST = env('POSTGRES_HOST', cast=str, default='localhost')
    POSTGRES_PORT = env('POSTGRES_PORT', cast=str, default='5432')
    POSTGRES_DB = env('POSTGRES_DB', cast=str)
    SECRET_KEY = env('SECRET_KEY', cast=str)
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECURITY_PASSWORD_SALT = env('SECURITY_PASSWORD_SALT', cast=str)
    DEBUG = env.bool('DEBUG')
    MAIL_SERVER = env('MAIL_SERVER', cast=str)
    MAIL_PORT = env('MAIL_PORT', cast=int)
    MAIL_USE_TLS = env.bool('MAIL_USE_TLS')
    MAIL_USE_SSL = env.bool('MAIL_USE_SSL')
    MAIL_DEBUG = env.bool('MAIL_DEBUG')
    MAIL_USERNAME = env('MAIL_USERNAME', cast=str)
    MAIL_PASSWORD = env('MAIL_PASSWORD', cast=str)
    MAIL_DEFAULT_SENDER = env('MAIL_DEFAULT_SENDER', cast=str)
    MAIL_MAX_EMAILS = env('MAIL_MAX_EMAILS', cast=str)
    MAIL_SUPRESS_SEND = env.bool('MAIL_SUPRESS_SEND', default=0)
    MAIL_ASCII_ATTACHMENTS = env.bool('MAIL_ASCII_ATTACHMENTS', default=0)