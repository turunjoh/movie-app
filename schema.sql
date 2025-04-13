CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    content TEXT
);

CREATE TABLE Movies (
    id INTEGER PRIMARY KEY,
    title TEXT UNIQUE,
    genre TEXT,
    year integer,
    visited integer
);

CREATE TABLE Reviews (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES Users,
    movie_id INTEGER REFERENCES Movies,
    content TEXT,
    rating INTEGER
    date TEXT,
    visited integer
);

CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    name TEXT,
    email TEXT,
    password_hash TEXT
);

CREATE TABLE Comments (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES Users,
    movie_id INTEGER,
    review_id INTEGER,
    content TEXT,
    date_created TEXT,
    date_changed TEXT
);
