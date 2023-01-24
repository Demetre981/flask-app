from app import app, db_controls
from flask import request, render_template, url_for, redirect
import sqlite3

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/posts")
def posts():
    articles = db_controls.get_db()
    return render_template("posts.html", articles=articles)

@app.route("/posts/<int:id>")
def posts_detail(id):
    article = db_controls.get_db(id)
    return render_template("posts_detail.html", article=article)

    


@app.route("/posts/<int:id>/update", methods=["GET", "POST"])
def post_update(id):
    article = db_controls.get_db(id)
    if request.method == "POST":
        title = request.form["title"]
        intro = request.form["intro"]
        text = request.form["text"]
        msg = db_controls.add_updates(title, intro, text, id)
        return msg
        
    
    return render_template("post_update.html", article=article)




@app.route("/create_article", methods=["GET", "POST"])
def create_article():
    if request.method == "POST":
        title = request.form["title"]
        intro = request.form["intro"]
        text = request.form["text"]
        msg = db_controls.add_new_article(title, intro, text)
        return msg
        # return redirect('/')
    return render_template("create_article.html")





# if __name__ == "__main__":
#     app.run()
