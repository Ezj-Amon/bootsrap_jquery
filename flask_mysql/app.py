from flask import Flask, render_template,request
import pymysql

app = Flask(__name__)


@app.route("/add/user",methods=['GET','POST'])
def add_user():
    if request.method == "GET":
        return render_template("add_user.html")
    else:
        # print(request.form)
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        mobile = request.form.get('mobile')
        #1. 连接数据库
        conn = pymysql.connect(host="localhost",user="root",password="127956",database="flask_mysql")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #2. 执行SqL
        sql = "insert into fm(username,password,number) values(%s,%s,%s)"
        print(sql)
        cursor.execute(sql,[user,pwd,mobile])
        conn.commit()
        #3.关闭连接
        cursor.close()
        conn.close()
        return 'xxx'

if __name__ == '__main__':
    app.run()
    # print(int('123'))
