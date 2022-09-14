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
        query="SELECT u.username, u.password, u.email, r.role FROM user u INNER JOIN role r on u.id_role = r.id_role WHERE u.username='{}'".format(username)
        cur.execute(query)
        data=cur.fetchone()
        print(data)
        if data[1] == password:
            return data
        else: 
            return None

# QUERYS MOD EXHIBITION

    @classmethod
    def insert_exhibition(self, name_exhibition, author, created_at, information, image):
        try:
            cur=mysql.connection.cursor()
            query="INSERT INTO exhibition (name_exhibition,author,created_at,information,image) VALUES('{}','{}',{},'{}','{}',)".format(name_exhibition, author, created_at, information, image)
            cur.execute(query)
            return {'message': 'Added Successfully'}
        except Exception as e:
            return str(e)

    @classmethod
    def update_exhibition(self, id, name_exhibition, author, created_at, information, image):
        try:
            cur=mysql.connection.cursor()
            query="UPDATE exhibition SET (name_exhibition,author,created_at,information,image) VALUES('{}','{}',{},'{}','{}',) WHERE id_exhibition={}".format(name_exhibition, author, created_at, information, image,id)
            cur.execute(query)
            return {'message': 'Updated Successfully'}
        except Exception as e:
            return str(e)

    @classmethod
    def fetch_all_exhibition(self):
        cur=mysql.connection.cursor()
        query="SELECT * FROM exhibition"
        cur.execute(query)
        data = cur.fetchall()
        return data

    @classmethod
    def fetch_exhibition(self, id):
        cur=mysql.connection.cursor()
        query="SELECT * FROM exhibition where id_exhibition={}".format(id)
        cur.execute(query)
        data = cur.fetchone()
        return data

    @classmethod
    def delete_exhibition(self, id):
        cur=mysql.connection.cursor()
        query="DELETE FROM exhibition WHERE id={}".format(id)
        cur.execute(query)
        return {'message': 'Delete Successfully'}