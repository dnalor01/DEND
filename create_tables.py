import psycopg2
from sql_queries import create_table_queries, drop_table_queries

"""Creates the database

Creates a database connection and cursor, then drops any preexisting Sparkify 
database and creates a new one. Finally, the connection to the original database
is closed and a connection is made to the new database.
"""
def create_database():
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn

"""Drops the tables

Uses the drop table commands for all the tables of the database from the 
sql_queries file 
"""
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

"""Creates the tables

Uses the create table commands for all the tables of the database from the 
sql_queries file
"""
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

"""Main

This function runs on the start of the program
"""
def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()