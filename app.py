import json
import re
import os

from flask import Flask
from flask import request
from flask_cors import CORS

from Class.Goods import Goods
from Class.User import User
from Mysql import session, Base, engine

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, supports_credentials=True)


basedir = os.path.abspath(os.path.dirname(__file__))


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


@app.route('/QueryInfo', methods=['POST', 'GET'])
def queryInfo():
    if request.method == 'POST':
        postForm = json.loads(request.get_data(as_text=True))
        userId = postForm['userId']
        if not session.query(User).filter(User.userID == userId).all():
            return "IdNotFound", 400
        else:
            res = session.query(User).filter(User.userID == userId).first()
            return json.dumps({  # 返回json
                "userName": res.userName,
                "gender": res.gender,
                "district": res.district,
                "grade": res.grade,
                "tel": res.tel
            }, ensure_ascii=False)


@app.route('/QueryInfoChangeGender', methods=['POST', 'GET'])
def queryInfoChangeGender():
    if request.method == 'POST':
        postForm = json.loads(request.get_data(as_text=True))
        userId = postForm['userId']
        gender = postForm['gender']
        if not session.query(User).filter(User.userID == userId).all():
            return "IdNotFound", 400
        else:
            res = session.query(User).filter(User.userID == userId).first()
            res.gender = gender
            res.update()
            return json.dumps({  # 返回json
                "userName": res.userName,
                "gender": res.gender,
            }, ensure_ascii=False)


@app.route('/QueryInfoChangeDistrict', methods=['POST', 'GET'])
def queryInfoChangeDistrict():
    if request.method == 'POST':
        postForm = json.loads(request.get_data(as_text=True))
        userId = postForm['userId']
        district = postForm['district']
        if not session.query(User).filter(User.userID == userId).all():
            return "IdNotFound", 400
        else:
            res = session.query(User).filter(User.userID == userId).first()
            res.district = district
            res.update()
            return json.dumps({  # 返回json
                "userName": res.userName,
                "district": res.district,
            }, ensure_ascii=False)


@app.route('/QueryInfoChangeGrade', methods=['POST', 'GET'])
def queryInfoChangeGrade():
    if request.method == 'POST':
        postForm = json.loads(request.get_data(as_text=True))
        userId = postForm['userId']
        grade = postForm['grade']
        if not session.query(User).filter(User.userID == userId).all():
            return "IdNotFound", 400
        else:
            res = session.query(User).filter(User.userID == userId).first()
            res.grade = grade
            res.update()
            return json.dumps({  # 返回json
                "userName": res.userName,
                "grade": res.grade,
            }, ensure_ascii=False)


@app.route('/QueryInfoChangeTel', methods=['POST', 'GET'])
def queryInfoChangeTel():
    if request.method == 'POST':
        postForm = json.loads(request.get_data(as_text=True))
        userId = postForm['userId']
        tel = postForm['tel']
        if re.search('^[0-9]{11}$', tel) is None:
            return "LengthNotMatch", 401
        if not session.query(User).filter(User.userID == userId).all():
            return "IdNotFound", 400
        else:
            res = session.query(User).filter(User.userID == userId).first()
            res.tel = tel
            res.update()
            return json.dumps({  # 返回json
                "userName": res.userName,
                "tel": res.tel,
            }, ensure_ascii=False)


@app.route('/SubmitGood', methods=['POST', 'GET'])
def submitGood():
    if request.method == 'POST':
        postForm = json.loads(request.get_data(as_text=True))
        userId = postForm['userId']
        goodName = postForm['goodName']
        goodType = postForm['goodType']
        goodPrice = postForm['goodPrice']
        goodDescription = postForm['goodDescription']
        goodLike = 0
        goodDislike = 0
        if not session.query(User).filter(User.userID == userId).all():
            return "IdNotFound", 400
        else:
            goods = Goods(sellerId=userId, goodName=goodName, goodType=goodType,
                          goodPrice=goodPrice, goodDescription=goodDescription, goodLike=goodLike, goodDislike=goodDislike)
            goods.save()
            userId = str(goods.sellerId)
            return json.dumps({  # 返回json
                "userID": int(userId)
            }, ensure_ascii=False)


@app.route('/ImageUpload', methods=['POST', 'GET'])
def imageUpload():
    if request.method == 'POST':
        postForm = json.loads(request.get_data(as_text=True))
        userId = postForm['userId']



@app.route('/QueryUserGoods', methods=['POST', 'GET'])
def queryUserGoods():
    if request.method == 'POST':
        postForm = json.loads(request.get_data(as_text=True))
        userId = postForm['userId']
        if not session.query(User).filter(User.userID == userId).all():
            return "IdNotFound", 400
        else:
            goods = session.query(Goods).filter(Goods.sellerId == userId).all()
            userName = session.query(User).filter(User.userID == userId).first().userName
            ansList = []
            for good in goods:
                goodType = ''
                if good.goodType == '1':
                    goodType = "电子类"
                elif good.goodType == '2':
                    goodType = "学习类"
                elif good.goodType == '3':
                    goodType = "食品类"
                ansList.append({
                    # "userName": userName,
                    "goodName": good.goodName,
                    "goodId": good.goodId,
                    # "goodType": good.goodType,
                    # "goodPrice": good.goodPrice,
                    "goodAbstract": "卖家：" + userName + "  |  " + "商品类别：" + goodType
                                    + "  |  " + "售价：￥" + str(good.goodPrice),
                    "goodDescription": good.goodDescription,
                    "goodLike": good.goodLike,
                    "goodDislike": good.goodDislike
                })
            goods_json = json.dumps(ansList, ensure_ascii=False)
            return goods_json


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug='true')
