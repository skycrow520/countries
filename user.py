""""Class User"""

import sql
import db

class User:
    """User"""

    def __init__(self, data: db.DataBase, uid: str):
        self.uid = uid
        self.obj = data.cursor()
        
