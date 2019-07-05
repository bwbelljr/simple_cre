# Importing SQLite packages
import sqlite3
from sqlite3 import Error
import os

# Specify database file
database_file = os.getcwd()+"\causal_test1.db"

def create_database(db_file):
    """ create a database connection to a SQLite database"""
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified  by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_causal(conn, causal):
    """
    Add a new causal tuple relation into the causal table
    :param conn:
    :param causal:
    :return: causal id
    """
    sql = ''' INSERT INTO causal(cause,effect,source)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, causal)
    return cur.lastrowid

def insert_causal_table(cause, effect, source):
    # create a database connections
    conn = create_connection(database_file)
    with conn:
        # create a new causal tuple relation
        causal = (cause, effect, source);
        causal_id = create_causal(conn, causal)

# Create SQLite database on disk (if not created)
create_database(database_file)

# Define causal table for database
sql_create_causal_table = """ CREATE TABLE IF NOT EXISTS causal
(
                              id integer PRIMARY KEY,
                              cause text NOT NULL,
                              effect text NOT NULL,
                              source text NOT NULL
                            ); """

# create causal table in database (if not created)
conn = create_connection(database_file)
if conn is not None:
    # create causal table
    create_table(conn, sql_create_causal_table)
else:
    print("Error! cannot create the database connection.")
