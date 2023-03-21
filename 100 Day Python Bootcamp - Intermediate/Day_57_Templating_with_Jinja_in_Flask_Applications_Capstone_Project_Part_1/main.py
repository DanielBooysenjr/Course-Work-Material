from flask import Flask, render_template
from post import Post

blog = Post()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=blog.blog_posts())


@app.route('/post/1')
def first_blog():
    return render_template("post.html", num=0 , posts=blog.blog_posts())

@app.route('/post/2')
def second_blog():
    return render_template("post.html", num=1, posts=blog.blog_posts())

if __name__ == "__main__":
    app.run(debug=True)

