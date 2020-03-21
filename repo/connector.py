import sqlalchemy
# function to init Connector Mariadb object
def init_connector(user, pass_word, host, database):
    uri = 'mysql+pymysql://{}:{}@{}/{}'
    engine = sqlalchemy.create_engine(uri.format(user,pass_word, host, database), echo=True)
    return engine