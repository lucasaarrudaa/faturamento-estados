import psycopg2

class Postgres:
    
    def __init__(self, host, port, dbase, user, pswrd):
        
        self.host = host
        self.port = port
        self.dbase = dbase
        self.user = user
        self.password = pswrd 

        
    def conecta(self):
        
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            dbase=self.dbase,
            user=self.user,
            password=self.password
        )
        self.cursor = self.conn.cursor()
        print("Connected to database.")