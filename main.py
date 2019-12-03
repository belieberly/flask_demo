from flask import Flask
from config import DevConfig

app = Flask(__name__)

#加载devconfig的变量集合，而不需要一项一项加载
app.config.from_object(DevConfig)


#指定URL = '的路由规则
@app.route('/')
def index():
    return 'index page'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


if __name__ == '__main__':
    app.run()
