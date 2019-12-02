from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index page'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


if __name__ == '__main__':
    app.run()
