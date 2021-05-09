from flask import Flask, render_template
import docker
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

client = docker.from_env()

@app.route('/')
@app.route('/home')
def home_page():
    dockerList = client.containers.list(all=True)
    docker_services = []
    for item in dockerList:
        if(item.status == "running" or item.status == "exited") :
            docker_services.append(
                {'containerId' : item.id[0:11], 
                'names' : item.name,
                'status' : item.status})

    return render_template('home.html', docker_services=docker_services)

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/startservice')
def start_service():
    return render_template("startservice.html")

if __name__ == "__main__":
    app.run(debug=True)