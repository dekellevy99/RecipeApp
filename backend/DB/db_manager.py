import pymysql
from . import sql_queries_constants

DEFAULT_HOST = "localhost"
DEFAULT_USER = "root"
DEFAULT_PWD = ""
DEFAULT_DB = "recipeappdb"


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

        self._init_tables()

    def _init_tables(self):
        dairy_ingredients = ["Cream","Cheese","Milk","Butter","Creme","Ricotta","Mozzarella","Custard","Cream Cheese"]
        gluten_ingredients = ["Flour","Bread","spaghetti","Biscuits","Beer"]
        with self.connection.cursor() as cursor:
            cursor.executemany(sql_queries_constants.INSERT_DAIRY_INGREDIANT, dairy_ingredients)
            cursor.executemany(sql_queries_constants.INSERT_GLUTEN_INGREDIANT, gluten_ingredients)
            self.connection.commit()

    def get_dairy_ingrediants(self):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.GET_DAIRY_INGREDIANTS)
            result = [ingrediant["name"] for ingrediant in cursor.fetchall()]
            return result

    def get_gluten_ingrediants(self):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_queries_constants.GET_GLUTEN_INGREDIANTS)
            result = [ingrediant["name"] for ingrediant in cursor.fetchall()]
            return result


db_manager = DB_Manager()