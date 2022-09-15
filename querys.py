import time
from main import mysql

# Querys DataBase.
class Query():

    #-----------------------------
    #|       Querys Login        |
    #-----------------------------

    @classmethod
    def insert_user(self,username,password,email):
        try:
            cur=mysql.connection.cursor()
            query="INSERT INTO user (username,password,email,id_role) VALUES('{}','{}','{}',2)".format(username,password,email)
            cur.execute(query)
            mysql.connection.commit()
            time.sleep(2.4)
            query="SELECT u.id_user, u.username, u.password, u.email, r.role FROM user u INNER JOIN role r on u.id_role = r.id_role WHERE u.username='{}'".format(username)
            cur.execute(query)
            data=cur.fetchone()
            print(data)
            if data[2] == password:
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
            query="SELECT u.id_user, u.username, u.password, u.email, r.role FROM user u INNER JOIN role r on u.id_role = r.id_role WHERE u.username='{}'".format(username)

        elif email != None:
            query="SELECT u.id_user, u.username, u.password, u.email, r.role FROM user u INNER JOIN role r on u.id_role = r.id_role WHERE u.email='{}'".format(email)

        cur.execute(query)
        data=cur.fetchone()
        if data == None:
            return True
        else:
            return False

    @classmethod
    def fetch_user_login(self, username,password):
        cur=mysql.connection.cursor()
        query="SELECT u.id_user, u.username, u.password, u.email, r.role FROM user u INNER JOIN role r on u.id_role = r.id_role WHERE u.username='{}'".format(username)
        cur.execute(query)
        mysql.connection.commit()
        data=cur.fetchone()
        if data[2] == password:
            return data
        else: 
            return None

    #------------------------------------
    #|        Querys exhibition         |
    #------------------------------------
    @classmethod
    def insert_exhibition(self, name_exhibition, author, created_at, information, image):
        try:
            cur=mysql.connection.cursor()
            query="INSERT INTO exhibition (name_exhibition,author,created_at,information,image) VALUES('{}','{}','{}','{}','{}')".format(name_exhibition, author, created_at, information, image)
            cur.execute(query)
            mysql.connection.commit()
            return {'message': 'Added Successfully'}
        except Exception as e:
            return str(e)

    @classmethod
    def update_exhibition(self, id, name_exhibition, author, created_at, information, image):
        try:
            cur=mysql.connection.cursor()
            query="UPDATE exhibition SET name_exhibition = '{}', author = '{}', created_at = '{}', information = '{}', image = '{}' WHERE exhibition.id_exhibition={}".format(name_exhibition, author, created_at, information, image,id)
            cur.execute(query)
            mysql.connection.commit()
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
        query="DELETE FROM exhibition WHERE id_exhibition={}".format(id)
        cur.execute(query)
        mysql.connection.commit()
        return {'message': 'Delete Successfully'}

    #------------------------------------
    #|        Querys Guided Tours       |
    #------------------------------------

    @classmethod
    def fetch_all_guided_tours(self):
        cur=mysql.connection.cursor()
        query="SELECT gd.id_guided_tours, gd.name_guided_tours, gd.description, sc.hour_start, sc.hour_end, sc.days FROM `guided_tours` gd INNER JOIN `schedule` sc ON gd.id_schedule = sc.id_schedule"
        cur.execute(query)
        data = cur.fetchall()
        return data

    @classmethod
    def fetch_guided_tour(self, id):
        cur=mysql.connection.cursor()
        query="SELECT gd.id_guided_tours, gd.name_guided_tours, gd.description, sc.hour_start, sc.hour_end, sc.days FROM `guided_tours` gd INNER JOIN `schedule` sc ON gd.id_schedule = sc.id_schedule WHERE id_guided_tours = {}".format(id)
        cur.execute(query)
        data = cur.fetchone()
        return data

    @classmethod
    def insert_visit(self,id_guided_tours, id_user, reference_name):
        cur=mysql.connection.cursor()
        query="INSERT INTO visit (id_guided_tours,id_user,reference_name) VALUES({},{},'{}')".format(id_guided_tours, id_user, reference_name)
        cur.execute(query)
        mysql.connection.commit()
        return {'message': 'Added Successfully'}

    @classmethod
    def delete_visit(self, id):
        cur=mysql.connection.cursor()
        query="DELETE FROM visit WHERE id_visit={}".format(id)
        cur.execute(query)
        mysql.connection.commit()
        return {'message': 'Delete Successfully'}

    @classmethod
    def fetch_all_visit(self, id):
        cur=mysql.connection.cursor()
        query="SELECT vs.id_visit, gd.name_guided_tours, gd.description , vs.reference_name FROM `visit` vs INNER JOIN `guided_tours` gd ON vs.id_guided_tours = gd.id_guided_tours INNER JOIN `user` u ON vs.id_user = u.id_user WHERE vs.id_user ={}".format(id)
        cur.execute(query)
        data = cur.fetchall()
        return data

    #------------------------------------
    #|        Querys review             |
    #------------------------------------

    @classmethod
    def fetch_all_review(self, id):
        cur=mysql.connection.cursor()
        query="SELECT r.id_review, u.username, r.score, r.message FROM review r INNER JOIN user u ON r.id_user = u.id_user INNER JOIN exhibition e ON e.id_exhibition = {}}".format(id)
        cur.execute(query)
        data = cur.fetchall()
        return data

    @classmethod
    def update_review(self, score, message, id):
        try:
            cur=mysql.connection.cursor()
            query="UPDATE review SET score={}, message='{}' WHERE id_review={}".format(score, message, id)
            cur.execute(query)
            mysql.connection.commit()
            return {'message': 'Updated Successfully'}
        except Exception as e:
            return str(e)

    @classmethod
    def insert_review(self, id, id_user, score, message):
        cur=mysql.connection.cursor()
        query="INSERT INTO review (id_exhibition, id_user, score, message VALUES ({},{},{},'{}'))".format(id, id_user, score, message)
        cur.execute(query)
        mysql.connection.commit()
        return {'message': 'Added Successfully'}

    @classmethod
    def delete_review(self, id):
        cur=mysql.connection.cursor()
        query="DELETE FROM review WHERE id_review={}".format(id)
        cur.execute(query)
        mysql.connection.commit()
        return {'message': 'Delete Successfully'}