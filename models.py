import sqlite3
from sqlite3 import Error
from os import path


db_file = path.abspath(path.dirname(__file__))
db_file = path.join(db_file, 'db.db')

sql_create_users_table = """ CREATE TABLE IF NOT EXISTS "users" (
                            "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                            "user" text NOT NULL,
                            "password" text,
                            "adress" text,
                            "money" integer,
                            "isadmin" integer); """

sql_create_products_table = """ CREATE TABLE IF NOT EXISTS "products" (
                            "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                            "name" text,
                            "price" int,
                            "img" text,
                            "colour" text
                            );"""

sql_create_bucket_table = """CREATE TABLE IF NOT EXISTS "bucket" (
                            "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                            "user" text NOT NULL,
                            "product" text
                            );"""

sql_insert_products_table = """INSERT INTO products (id, name, price, img, colour) VALUES 
                                        ('5', 'Кольцевой ключ', '400', NULL, NULL),
                                        ('4', 'Торцовый ключ', '100', NULL, NULL),
                                        ('3', 'Разводной ключ', '300', NULL, NULL),
                                        ('2', 'Гаечный ключ', '200', NULL, NULL),
                                        ('1', 'Молоток', '1500', NULL, NULL);
                                        """

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        c.fetchall()
    except Error as e:
        print(e)

def insert_data_to_table(conn,expression):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        cur = conn.cursor()
        cur.execute(expression)
        row = cur.fetchall()
        conn.commit()
        print(row)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def createDB():
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_products_table)
        create_table(conn, sql_create_bucket_table)
        insert_data_to_table(conn, sql_insert_products_table)
         
    if not path.exists(db_file):
        def create_connection(db_file):
            conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

#Продукты
def getProduct(id):
    conn=create_connection(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * from products where id=?",(id))
    row = cur.fetchall()
    return row
def getAllProducts():
    conn = ""
    try:
       conn=sqlite3.connect(db_file)
       cur = conn.cursor()
       cur.execute("SELECT * from products")
       row = cur.fetchall()
       return row
    except Error as e:
       print(e)
    finally:
        if conn:
            conn.close()
#Корзина
def getBasket(user):
    conn=sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * from bucket where user=?",(user,))
    row = cur.fetchall()
    return row
    
def insertProductsToBasket(user,product):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        cur = conn.cursor()
        cur.execute("INSERT into bucket (user,product) values (?,?);",(user,product))
        row = cur.fetchall()
        cur.execute("select * from bucket;")
        row = cur.fetchall()
        conn.commit()
        print(row)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

#Пользователи
def insertUser(user,password):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        cur = conn.cursor()
        cur.execute("INSERT into users(user,password) values (?,?);",(user,password))
        row = cur.fetchall()
        conn.commit()
        print(row)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def getUser(user):
    row = ""
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        cur = conn.cursor()
        cur.execute("SELECT * from users where user=?",(user,))
        row = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            return row
def getUserID(user):
    row = ""
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        cur = conn.cursor()
        cur.execute("SELECT id from users where user=?",(user,))
        row = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            return row
   

