import streamlit as st
from contextlib import contextmanager
import mysql.connector
from mysql.connector import IntegrityError


@contextmanager
def get_connection():
    try:
        conn = mysql.connector.connect(
            host=st.secrets["mysql"]["host"],
            port=st.secrets["mysql"]["port"],
            database=st.secrets["mysql"]["database"],
            user=st.secrets["mysql"]["user"],
            password=st.secrets["mysql"]["password"]
        )

        yield conn
        conn.commit()

    finally:
        if "conn" in locals():
            conn.close()


def init_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    role VARCHAR(20) DEFAULT 'user'
                );
            """)


def create_user(username, email, password_hash):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO users
                    (username, email, password_hash)
                    VALUES (%s, %s, %s)
                    """,
                    (username, email, password_hash)
                )

        return True

    except IntegrityError:
        return False


def get_user_by_username(username):
    with get_connection() as conn:
        with conn.cursor(dictionary=True) as cur:
            cur.execute(
                "SELECT * FROM users WHERE username = %s",
                (username,)
            )
            return cur.fetchone()


def get_all_users():
    with get_connection() as conn:
        with conn.cursor(dictionary=True) as cur:
            cur.execute(
                """
                SELECT id, username, email, created_at, role
                FROM users
                ORDER BY id
                """
            )
            return cur.fetchall()


def user_exists(username=None, email=None):
    with get_connection() as conn:
        with conn.cursor(dictionary=True) as cur:

            if username:
                cur.execute(
                    "SELECT 1 FROM users WHERE username = %s",
                    (username,)
                )

            elif email:
                cur.execute(
                    "SELECT 1 FROM users WHERE email = %s",
                    (email,)
                )

            return cur.fetchone() is not None


def update_password(username, new_hash):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE users
                SET password_hash = %s
                WHERE username = %s
                """,
                (new_hash, username)
            )