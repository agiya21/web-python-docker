from flask import Flask, render_template
import docker
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET KEY'] = '71ae825c2f5e265aad1ad956'
db = SQLAlchemy(app)
client = docker.from_env()

## CLASSES FOR COMPONENTS
class Webaccount(db.Model):
    uname = db.Column(db.String(length=10), primary_key=True)
    passwd = db.Column(db.String(length=8), nullable=False)

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField(label='password')
    submit = SubmitField(label='submit')


## VIEW CONTENT
@app.route('/')
@app.route('/home')
def home_page():
    dockerList = client.containers.list(all=True)
    docker_services = []
    for item in dockerList:
        docker_services.append(
            {'containerId' : item.id[0:11], 
             'names' : item.name,
             'status' : item.status})

    return render_template('home.html', docker_services=docker_services)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/startservice')
def start_service():
    return render_template("startservice.html")



## RUN FLASK IN DEBUG MODE
if __name__ == "__main__":
    app.run(debug=True)