class Config():
    SECRET_KEY = 'sdfkaj;lsdjf;ahs;lkh;'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flasklogin'

config={
    'development':DevelopmentConfig
}