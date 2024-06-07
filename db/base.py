import sqlite3


def create_connection():  # ! Create connection to database
    conn = sqlite3.connect('database.db')
    return conn

def create_table():  # ! Create table for audios
    conn = create_connection()  # ! Create connection
    cursor = conn.cursor()  # ! Create cursor
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS original_audios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        executor TEXT NOT NULL,
        genre VARCHAR NOT NULL
    );
    CREATE TABLE IF NOT EXISTS features_vectors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        audio_id INTEGER NOT NULL,
        feature_vector BLOB NOT NULL,
        FOREIGN KEY (audio_id) REFERENCES original_audios (id)
    );
    ''')
    conn.commit()  # ! Save changes
    conn.close()  # ! Close connection


def insert_audio(name, executor, genre):  # ! Insert audio to database
    conn = create_connection()  # ! Create connection
    cursor = conn.cursor()  # ! Create cursor
    cursor.execute('''
    INSERT INTO original_audios (name, executor, genre) VALUES (?, ?, ?) 
    ''', (name, executor, genre))
    conn.commit()  # ! Save changes
    conn.close()  # ! Close connection


def get_audios():  # ! Get all audios from database
    conn = create_connection()  # ! Create connection
    cursor = conn.cursor()  # ! Create cursor
    cursor.execute('''
    SELECT * FROM original_audios
    ''')
    audios = cursor.fetchall()
    conn.close()  # ! Close connection
    return audios

