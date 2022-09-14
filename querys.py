import time
from main import mysql

class Query():
    @classmethod
    def insert_user(self,username,password,email):
        try:
            cur=mysql.connection.cursor()
            query="INSERT INTO user (username,password,email,id_role) VALUES('{}','{}','{}',2)".format(username,password,email)
            cur.execute(query)
            mysql.connection.commit()
            time.sleep(2.4)
            query="SELECT u.username, u.password, u.email, r.role FROM user u INNER JOIN role r on u.id_role = r.id_role WHERE u.username='{}'".format(username)
            cur.execute(query)
            data=cur.fetchone()
            print(data)
            if data[1] == password:
                return data
            else: 
                return None
        except Exception as e:
            return str(e)

    @classmethod
    def fechtAllUsers(self):
        cur=mysql.connection.cursor()
        query="SELECT * FROM user"
        cur.execute(query)
        data = cur.fetchall()
        print(data)
        return data

    @classmethod
    def fetch_user_signup(self, username, email):
        cur=mysql.connection.cursor()

        if username != None:
            query="SELECT u.email, u.password, u.email, r.role FROM user u INNER JOIN role r on u.id_role = r.id_role WHERE u.username='{}'".format(username)

        elif email != None:
            query="SELECT u.email, u.password, u.email, r.role FROM user u INNER JOIN role r on u.id_role = r.id_role WHERE u.email='{}'".format(email)

        cur.execute(query)
        data=cur.fetchone()
        if data == None:
            return True
        else:
            return False

    @classmethod
    def fetch_user_login(self, username,password):
        cur=mysql.connection.cursor()
        print(username, password, "hola")
        query="SELECT u.username, u.password, u.email, r.role FROM user u INNER JOIN role r on u.id_role = r.id_role WHERE u.username='{}'".format(username)
        cur.execute(query)
        data=cur.fetchone()
        print(data)
        if data[1] == password:
            return data
        else: 
            return None