from flask import Flask,render_template,url_for
from datetime import date
import requests


app = Flask(__name__)

@app.route("/")
def home():
    y = date.today().year
    return render_template("index.html",year=y)

@app.route("/guess/<name>")
def process(name):
    parameter = {
        "name": name
    }
    gender_of_the_person = requests.get(url="https://api.genderize.io", params=parameter).json()["gender"]
    age_of_the_person = requests.get(url="https://api.agify.io", params=parameter).json()["age"]
    return render_template("api_area.html",name=name,gender=gender_of_the_person,age=age_of_the_person)

@app.route("/blog")
def blog_posts():
    all_posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html",posts=all_posts)

@app.route("/blog/<int:id>")
def post(id):
    all_posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("post.html",posts=all_posts,id=id)


if __name__ == "__main__":
    app.run(debug=True)

