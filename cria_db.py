import psycopg2
from conexao_db import Postgres

class CriaBanco:
    
    def __init__(self):
        
        self.conn = Postgres(host="localhost",
                        port="15430",
                        dbase="postgres",
                        user="postgres",
                        pswrd="Postgres").conecta()

    def create_db(self):
        # Connects to the Docker database
        conn = psycopg2.connect(self.conn)

        # Sets autocommit to True
        conn.autocommit = True
        
        # Checks if the database already exists
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM pg_database WHERE datname='teste'")
        exists = cur.fetchone()
        
        # If the database doesn't exist, creates it
        if not exists:
            cur.execute("CREATE DATABASE teste;")
            print("Database created successfully!")
        else:
            print("Database already exists.")
        
        # Closes the connection
        cur.close()
        conn.close()

if __name__ == "__main__":
    CriaBanco().create_db()
