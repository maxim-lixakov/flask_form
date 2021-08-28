from flask import Flask, render_template, request
from flask_migrate import Migrate
from models import db, User, User_data
import os
from dotenv import load_dotenv
from langdetect import detect


load_dotenv()
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
user = os.getenv("user")
pswd = os.getenv("password")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{pswd}@localhost:5432/domeo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        name = request.form['userName']
        middle_name = request.form['userSurname']
        bornData = request.form['dateBorn']
        gender = request.form['gender']
        new_user = User(name=name, middle_name=middle_name,
                        bornData=bornData, gender=gender)
        db.session.add(new_user)
        db.session.commit()
        # -----------------user_data------------------
        citizenship = request.form['citizen']
        comment = request.form['comment']
        education = request.form['education']
        user_data = User_data(citizenship=citizenship, comment=comment,
                              education=education, user_id=new_user.id)
        db.session.add(user_data)
        db.session.commit()
    return render_template("picture.html")


if __name__ == '__main__':
    app.run()
