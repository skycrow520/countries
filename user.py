""""Class User"""

import sql
import db

class User:
    """User"""

    def __init__(self, data: db.DataBase, uid: str):
        self.uid = data.cursor.excute(sql.SELECT.format\
                (table_name='user', query_key='uid', query_val=uid))
