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

        #2. 执行SqL

        #3.关闭连接

        return 'xxx'

if __name__ == '__main__':
    app.run()
