class Config(object):
    """base config class"""
    pass



class ProdConfig(Config):
    """"Production config class"""
    pass


class DevConfig(Config):
    """Development config class"""
    # open the debug
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ilynsm77@127.0.0.1:3306/flask_demo'