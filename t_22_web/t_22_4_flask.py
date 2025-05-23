from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Home</h1>"


@app.route('/sign', methods=['GET'])
def sign():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    print('request.method', request.method)
    if request.form.get('username') == 'admin' and request.form['password'] == 'password':
        return '<h3>hello admin</h3>'
    return '<h3> bad username or password</h3>'


if __name__ == '__main__':
    app.run(debug=True)
