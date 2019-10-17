import sqlite3

class Base(object):
 
    def get_connection(self):
        return sqlite3.connect('database/appdoape.db')
    
    def create_tables(self):
        conn = self.get_connection()
        conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS USER 
        (ID_USER INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL);
        '''    
        )
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
        ID_USER INT NOT NULL,
        FOREIGN KEY(ID_MONTH) REFERENCES MONTH(ID_MONTH),
        FOREIGN KEY(ID_USER) REFERENCES USER(ID_USER));
        '''
        )
        conn.close()
        print('TABELAS CRIADAS!!!')
    
    def insert_tables(self):
        self.insert_users()
        self.insert_months()
        self.insert_payers()
        self.close_conn()

    def insert_users(self):
        conn = self.get_connection()
        conn.execute("INSERT INTO USER (ID_USER,NAME) VALUES (1, 'João')")
        conn.execute("INSERT INTO USER (ID_USER,NAME) VALUES (2, 'Júlio')")
        conn.execute("INSERT INTO USER (ID_USER,NAME) VALUES (3, 'Marcos')")
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
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_USER) VALUES (1, 2)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_USER) VALUES (2, 3)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_USER) VALUES (3, 1)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_USER) VALUES (4, 2)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_USER) VALUES (5, 3)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_USER) VALUES (6, 1)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_USER) VALUES (7, 2)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_USER) VALUES (8, 3)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_USER) VALUES (9, 1)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_USER) VALUES (10, 2)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_USER) VALUES (11, 3)")
        conn.execute("INSERT INTO PAYER (ID_MONTH,ID_USER) VALUES (12, 1)")
        conn.commit()
        conn.close()

    def get_users(self):
        conn = self.get_connection()
        sql = "SELECT name FROM USER"
        users = conn.execute(sql).fetchall()
        return [user[0] for user in users]

    def get_payers(self):
        conn = self.get_connection()
        sql = "SELECT MONTH.MONTH, USER.NAME FROM PAYER JOIN USER USING (ID_USER) JOIN MONTH USING (ID_MONTH)"
        payers = conn.execute(sql).fetchall()
        return {payer[0]:payer[1] for payer in payers}


    def close_conn(self):
        self.get_connection().close()