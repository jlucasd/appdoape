import sqlite3

class Base(object):
 
    def get_connection(self):
        return sqlite3.connect('database/appdoape.db')
    
    def create_tables(self):
        conn = self.get_connection()
        conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS RESIDENT 
        (ID_RESIDENT INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL);
        '''    
        )
        conn.execute('''CREATE TABLE IF NOT EXISTS USER 
        (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,	
        USERNAME VARCHAR(120) NOT NULL,	
        PASSWORD_HASH VARCHAR(128) NOT NULL)''')	
        conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS PAYMENT
        (ID_PAYMENT INT PRIMARY KEY NOT NULL,
        USER TEXT NOT NULL);
        '''
        )
        conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS MONTH
        (ID_MONTH INT PRIMARY KEY NOT NULL,
        MONTH TEXT NOT NULL);
        '''
        )
        conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS PAYER(
        ID_MONTH INT NOT NULL, 
        ID_RESIDENT INT NOT NULL,
        FOREIGN KEY(ID_MONTH) REFERENCES MONTH(ID_MONTH),
        FOREIGN KEY(ID_RESIDENT) REFERENCES USER(ID_RESIDENT));
        '''
        )
        conn.close()
    
    def insert_users(self):
        conn = self.get_connection()
        conn.execute("INSERT INTO USER (ID, USERNAME, PASSWORD_HASH)"+ 
        " VALUES (1, 'apesenai', 'pbkdf2:sha256:150000$rpfH8uqx$0008ce779ff827a842b5292fe28d86b95885cb61e4a6add85a2312ecc881939a')")
        conn.commit()
        conn.close()

    def insert_residents(self):
        conn = self.get_connection()
        conn.execute("INSERT INTO RESIDENT (ID_RESIDENT,NAME) VALUES (1, 'João')")
        conn.execute("INSERT INTO RESIDENT (ID_RESIDENT,NAME) VALUES (2, 'Júlio')")
        conn.execute("INSERT INTO RESIDENT (ID_RESIDENT,NAME) VALUES (3, 'Marcos')")
        conn.commit()
        conn.close()

    def insert_months(self):
        conn = self.get_connection()
        conn.execute("INSERT INTO MONTH (ID_MONTH,MONTH) VALUES (1, 'Janeiro')")
        conn.execute("INSERT INTO MONTH (ID_MONTH,MONTH) VALUES (2, 'Fevereiro')")
        conn.execute("INSERT INTO MONTH (ID_MONTH,MONTH) VALUES (3, 'Março')")
        conn.execute("INSERT INTO MONTH (ID_MONTH,MONTH) VALUES (4, 'Abril')")
        conn.execute("INSERT INTO MONTH (ID_MONTH,MONTH) VALUES (5, 'Maio')")
        conn.execute("INSERT INTO MONTH (ID_MONTH,MONTH) VALUES (6, 'Junho')")
        conn.execute("INSERT INTO MONTH (ID_MONTH,MONTH) VALUES (7, 'Julho')")
        conn.execute("INSERT INTO MONTH (ID_MONTH,MONTH) VALUES (8, 'Agosto')")
        conn.execute("INSERT INTO MONTH (ID_MONTH,MONTH) VALUES (9, 'Setembro')")
        conn.execute("INSERT INTO MONTH (ID_MONTH,MONTH) VALUES (10, 'Outubro')")
        conn.execute("INSERT INTO MONTH (ID_MONTH,MONTH) VALUES (11, 'Novembro')")
        conn.execute("INSERT INTO MONTH (ID_MONTH,MONTH) VALUES (12, 'Dezembro')")
        conn.commit()
        conn.close()

    def insert_payers(self):
        conn = self.get_connection()
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_RESIDENT) VALUES (1, 2)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_RESIDENT) VALUES (2, 3)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_RESIDENT) VALUES (3, 1)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_RESIDENT) VALUES (4, 2)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_RESIDENT) VALUES (5, 3)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_RESIDENT) VALUES (6, 1)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_RESIDENT) VALUES (7, 2)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_RESIDENT) VALUES (8, 3)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_RESIDENT) VALUES (9, 1)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_RESIDENT) VALUES (10, 2)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_RESIDENT) VALUES (11, 3)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_RESIDENT) VALUES (12, 1)")
        conn.commit()
        conn.close()

    def get_residents(self):
        conn = self.get_connection()
        sql = "SELECT name FROM RESIDENT"
        residents = conn.execute(sql).fetchall()
        return [resident[0] for resident in residents]

    def get_payers(self):
        conn = self.get_connection()
        sql = "SELECT MONTH.MONTH, RESIDENT.NAME FROM PAYER JOIN RESIDENT USING (ID_RESIDENT) JOIN MONTH USING (ID_MONTH)"
        payers = conn.execute(sql).fetchall()
        return {payer[0]:payer[1] for payer in payers}


    def close_conn(self):
        self.get_connection().close()
    
    def create_database(self):
        self.create_tables()
        print('TABELAS CRIADAS!!!')
        self.insert_users()
        self.insert_residents()
        self.insert_months()
        self.insert_payers()
        print('REGISTROS INSERIDOS!!!')
        self.close_conn()
