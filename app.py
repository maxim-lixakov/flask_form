from flask import Flask, render_template, request, send_file
from models import Base, User, User_data
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db_connect(wrapper_func):
    def wrapper():
        engine = create_engine(f"postgresql://{user}:{pswd}@194.67.203.117:5437/trainingTest")
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        wrapper_func(session)
        return ''
    return wrapper


load_dotenv()
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
user = os.getenv("user")
pswd = os.getenv("password")

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("picture.html")


@app.route('/getHTML', methods=['GET'])
def load_html():
    return send_file('templates/form.html')


@app.route('/postData', methods=['POST'])
@db_connect
def post_data(session):
    print(request.json)
    for key in request.json:
        name = request.json[key]['userName']
        middle_name = request.json[key]['userSurname']
        bornData = request.json[key]['dateBorn']
        gender = request.json[key]['gender']
        new_user = User(name=name, middle_name=middle_name,
                        bornData=bornData, gender=gender)
        session.add(new_user)
        session.commit()
        # -----------------user_data------------------
        print(request.json)
        if 'citizen' in request.json[key]:
            citizenship = request.json[key]['citizen']
        else:
            citizenship = ''
        if 'comment' in request.json[key]:
            comment = request.json[key]['comment']
        else:
            comment = ''
        if 'education' in request.json[key]:
            education = request.json[key]['education']
        else:
            education = ''
        phone = request.json[key]['phone']
        user_data = User_data(citizenship=citizenship, comment=comment,
                              education=education, user_id=new_user.id, phone=phone)
        session.add(user_data)
        session.commit()


if __name__ == '__main__':
    app.run()
