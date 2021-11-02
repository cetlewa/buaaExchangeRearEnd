import json
import pymysql

from flask import Flask
from flask import request
from flask_cors import CORS

from DataBase.module import session

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/Login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        postForm = json.loads(request.get_data(as_text=True))
        username = postForm['userName']
        password = postForm['password']

        print(session.query())
        print(postForm)
        return json.dumps({
            'userName': int(username)
        }, ensure_ascii=False)
    else:
        return "Error", 404


if __name__ == '__main__':
    app.run()
