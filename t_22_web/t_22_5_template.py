# 使用模版

from flask import Flask, request, render_template


print("__name__", __name__)
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form.get('password')
    if username == 'admin' and password == 'password':
        return render_template('signin_ok.html', usernameParam=username)
    return render_template('form.html', msg='用户名密码错误', usernameParam=username)


if __name__ == '__main__':
    app.run(debug=True)


