from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

posts = []

@app.route('/')
def home():
    global posts
    blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
    resposne = requests.get(blog_url)
    posts = resposne.json()
    random.shuffle(posts)
    print(posts)
    return render_template("index.html", posts=posts)

@app.route('/post/<num>')
def post(num):
    return render_template("post.html", post=posts[int(num)])

if __name__ == "__main__":
    app.run(debug=True)
