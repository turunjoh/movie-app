import sqlite3
from flask import g

def get_connection():
    con = sqlite3.connect("database.db")
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()

def last_insert_id():
    return g.last_insert_id    
    
def query(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result


def get_reviews(genre = None):
    if genre:
        res = query("select * from Reviews WHERE genre LIKE ?", f"%{genre.lower()}%")  
    else:
        res = query("select * from Reviews")
    return res

def get_movies():
    sql = """
SELECT * from movies
ORDER BY id desc
"""
    return query(sql)


#def init_d# luo tietokantaan tarvittavat taulut
def create_tables():
    db = get_connection()

    db.execute(
"""
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    content TEXT
)
""")
    
    db.execute(
"""
CREATE TABLE Movies (
    id INTEGER PRIMARY KEY,
    title TEXT UNIQUE,
    genre TEXT,
    year integer,
    visited integer
    )
""")
    db.execute(
"""
CREATE TABLE Reviews (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES Users,
    movie_id INTEGER REFERENCES Movies,
    content TEXT,
    rating INTEGER
    date TEXT,
    visited integer
    )
""")
    db.execute(
"""
CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    name TEXT,
    email TEXT,
    password_hash TEXT
    )
""")
    db.execute(
"""
CREATE TABLE Comments (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES Users,
    movie_id INTEGER,
    review_id INTEGER,
    content TEXT,
    date_created TEXT,
    date_changed TEXT
    )
""")
    db.close()





def list_tables():
    db = get_connection()
    res = list(db.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())
    db.close()
    return res

def list_reviews():
    db = get_connection()
    res = list(db.execute("SELECT title FROM Reviews").fetchall())
    db.close()
    return res



def add_user(username, password_hash):    
    execute("INSERT INTO Users (username, password_hash) VALUES (?, ?)", [username, password_hash])




def add_review(user_id: int, movie_id: int, content: str, rating: int):
    execute("INSERT INTO Reviews (user_id, movie_id, content, rating, created_at) VALUES (?, ?, ?, ?, NOW())",
            [user_id, movie_id, content, rating])


def add_comment(user_id: int, movie_id: int, review_id: int, content: str):
    execute("INSERT INTO Comments (user_id, movie_id, review_id, content, created_at) VALUES (?, ?, ?, NOW())", 
            [user_id, movie_id, review_id, content])
    



def add_movie(title: str, genre: str, year: int):
    execute(
"""
INSERT INTO Movies (title, genre, year) VALUES (?, ?, ?)
""", [title, genre, year])
    