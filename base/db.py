import sqlite3
import pymysql

# ======================== 数据库操作类 ========================
class Database:
    # def __init__(self):
    #     # 连接到数据库
    #     self.con = pymysql.connect(
    #                                 host=eval(mysql_dict.get("host")),
    #                                 user=mysql_dict.get("user"),
    #                                 password=mysql_dict.get("password"),
    #                                 port=int(mysql_dict.get("port")),
    #                                 db=mysql_dict.get("db"),
    #                                 charset="utf8")
    #     # 创建一个游标
    #     self.cur = self.con.cursor()
    #     logger.info(f"DB OK self.cur:{self.cur}")
    #     return
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cur = self.conn.cursor()
        self.create_table()
        return
    def __del__(self):
        self.conn.close()
        return

    def create_table(self):
        sql = ''' CREATE TABLE IF NOT EXISTS students ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT NOT NULL, 
                age INTEGER, 
                gender TEXT, 
                class_name TEXT 
            )'''
        self.cur.execute(sql)

        self.conn.commit()
        return

    def get_one(self, sql):
        """获取查询到的第一条数据"""
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_all(self, sql):
        """获取sql语句查询到的所有数据"""
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()


    def insert_rec(self, student_data):
        """获取sql语句查询到的所有数据"""

        self.cur.execute('''
                       INSERT INTO students (name, age, gender, class_name)
                       VALUES (?, ?, ?, ?)
                       ''', student_data)

        # 提交事务（确保数据写入数据库）
        self.conn.commit()
        print("数据库创建成功，表和记录插入完成！")
        return

    def count(self, sql):
        """获取sql语句查询到的所有数据"""
        self.conn.commit()
        res = self.cur.execute(sql)
        return res

    def close(self):
        # 关闭游标对象
        self.cur.close()
        # 断开连接
        self.conn.close()

# ======================== 运行程序 ========================
if __name__ == "__main__":
    db = Database()
    db.create_table()
    # student_data = ("张三", 16, "男", "高一(2)班")  # 待插入的数据
    # db.insert_rec(student_data)

    sql = "SELECT * FROM students"
    student_data = db.get_one(sql)
    print(student_data)

    student_data = db.get_all(sql)
    print(student_data)
