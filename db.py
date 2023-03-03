import flask_sqlalchemy

class DataBase:
    """DataBase类"""

    def __init__(self, host, port, user, passwd, db_name, charset):
        self.db = pymysql.connect(
            host=host, 
            port=port, 
            user=user, 
            password=passwd, 
            database=db_name, 
            charset=charset)
        
        self.cursor = self.db.cursor()
