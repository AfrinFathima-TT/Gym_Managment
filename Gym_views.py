from mysql import connector
import datetime
class DbConnect:
    def get_connected(self):
        try:
            self.connection = connector.connect(
                host = "localhost",
                user = "root",
                password = "Afreen@2004",
                database = "gym_db"
            )
            return self.connection
        except Exception as e:
            return None
class GymMemberManagement(DbConnect):
    def get_object(self,id=None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connection.cursor()
            query = "Select * from member where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None
    def get(self):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "select * from member"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            # print(records)
            for data in records:
                print(data)
        except Exception as e:
            print(e)
    def post(self,**kwargs):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "insert into member (Name,Place,Mobile,Plan,Fee,Joined_date) values (%s,%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print(" New Member added successfully...!")
        except Exception as e:
            print(e)
    def retrieve(self,id=None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "select *from member where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            print(record)                            ####return record
        except Exception as e:
            print (e)
    def delete(self,id = None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "select * from member where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            if record != None:
                query = " delete from member where id = %s"
                values = (id,)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Data deleted Successfully...!")
            else:
                print("Member not found...!")
        except Exception as e:
            print(e)
    def put(self,id = None,**kwargs):
        try:

            self.connect = super().get_connected()
            record = self.get_object(id = id)

            if record != None:
                self.cursor = self .connection.cursor()
                placeholder = ""
                for k in kwargs:
                    placeholder += k + "=%s,"
                placeholder = placeholder.rstrip(",")
                query = f"update member set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values . append(id)
                self.cursor.execute(query ,values)
                self.connection.commit()
                print("Member details updated successfully...!")
            else:
                print("Member not found...!")
        except Exception as e:
            print(e)



connection_instance = DbConnect()
print(connection_instance.get_connected())

member_instance = GymMemberManagement()
# member_instance.get()
# member_instance.post(Name = "Nayana",Place = "Thrissur",Mobile = "98904369762",Plan = "1 Month",Fee = 2000,Joined_date= datetime.datetime.today())
# member_instance.get()
print("_ _ _ _ Data of one member _ _ _ _")
member_instance.retrieve(id = 4)             ####print(member_instance.retrieve(4))
print("_ _ _ _ Deletion _ _ _ _")
member_instance.delete( id = 9)

# member_instance.get()
print("_ _ _ _ updation_ _ _ _")
member_instance.put(7,plan = "6 Month")