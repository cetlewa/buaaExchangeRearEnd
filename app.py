import json

from flask import Flask
from flask import request
from flask_cors import CORS
from Class.User import User
from Mysql import session, Base, engine

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, supports_credentials=True)


def getUserId(userName):
    return session.query(User.userID).filter(User.userName == userName).first()[0]

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/Login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        postForm = json.loads(request.get_data(as_text=True))
        userName = postForm['userName']
        password = postForm['password']
        if not session.query(User).filter(User.userName == userName).all():
            return "NotRegister", 400
        else:
            res = session.query(User.password).filter(User.userName == userName).first()
            pwd = res.password
            if pwd == password:
                userId = getUserId(userName)
                return json.dumps({
                    'userID': userId
                }, ensure_ascii=False)
            else:
                return "WrongPassWord", 400



@app.route('/Register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        postForm = json.loads(request.get_data(as_text=True))
        userName = postForm['userName']
        password = postForm['password']
        gender = postForm['gender']
        grade = postForm['grade']
        district = postForm['district']
        tel = postForm['tel']
        if not session.query(User).filter(User.userName == userName).all():
            user = User(userName=userName, password=password, gender=gender, grade=grade, district=district, tel=tel)
            user.save()
            userID = str(user.userID)
            return json.dumps({  # 返回json
                "userID": int(userID)
            }, ensure_ascii=False)
        else:
            return "RepeatName", 400



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print(Base)
    print(111)
    app.run(debug='true')
