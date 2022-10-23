import pymysql
from . import sql_queries_constants

DEFAULT_HOST = "localhost"
DEFAULT_USER = "root"
DEFAULT_PWD = ""
DEFAULT_DB = ""


class DB_Manager:
    def __init__(self, host = DEFAULT_HOST, user = DEFAULT_USER, pwd = DEFAULT_PWD, db = DEFAULT_DB):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=pwd,
            db=db,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )


db_manager = DB_Manager()