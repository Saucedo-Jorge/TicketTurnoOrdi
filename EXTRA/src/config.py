class Config:
    SECRET_KEY = 'jmhjtz9&nuvpemf!7wles2v!o_ubr4&obv-!=o#fx1u#u$klih'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1234'
    MYSQL_DB = 'ticket'
    
    
config={'development' : DevelopmentConfig}