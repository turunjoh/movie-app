from flask import Flask, render_template, request, redirect, session
import os
import sqlite3
import db
import config
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.secret_key = config.secret_key

#if os.path.exists("database.db"):
#    os.remove("database.db")

#db = sqlite3.connect("database.db")
#db.isolation_level = None






@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    
    sql = "SELECT password_hash FROM users WHERE username = ?"
    password_hash = db.query(sql, [username])

    #sql2 = "SELECT id FROM users WHERE username = ?"
    #id = db.query(sql2, [username])
    if len(password_hash) > 0:
        password_hash = password_hash[0][0]
    else:
        return "VIRHE: väärä tunnus tai salasana"
    

    if check_password_hash(password_hash, password):
        session["username"] = username
        #session["id"] = id
        return redirect("/")
    else:
        return "VIRHE: väärä tunnus tai salasana"



@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/reviews")
def list_reviews():
    rews = db.query("select * from Reviews")
    
    return render_template("reviews.html", rews=rews)






@app.route("/movies/<int:page_id>")
def page(page_id):
    movie = db.query("SELECT * FROM Movies WHERE id = ?", [page_id])
    print(movie)

    return f"{movie}"




@app.route("/")
def index():
    movies = db.get_movies()
    return render_template("index.html", movies = movies)


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        db.add_user(username=username, password_hash=password_hash)
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"


@app.route("/new_movie")
def new_movie():
    return render_template("new_movie.html")


@app.route("/add_movie", methods=["POST"])
def add_movie():
    title = request.form["title"]
    year = request.form["year"]
    genres = " ".join([request.form["genre1"], request.form["genre2"], request.form["genre3"]])
    #genres = request.form["genre1"]
    try:
        db.add_movie(title=title, genre=genres, year=year)
    except sqlite3.IntegrityError:
        return "VIRHE: Elokuva on jo olemassa"
    return "Elokuva luotu"



@app.route("/user/<username>")
def user_profile(username):
    user_movies = db.query("SELECT * FROM Reviews")
    movie_count = db.query("SELECT COUNT(*) FROM Movies")[0][0]
    return render_template("user.html", username=username, movies=user_movies, movie_count=movie_count)


#@app.route("/movies")
#def movies()