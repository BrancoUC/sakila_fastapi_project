import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.film_text import FilmText

class FilmTextController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_film_texts(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM film_text")
            rows = cursor.fetchall()
            cursor.close()
            return [FilmText(**row) for row in rows]
        except Error as e:
            print(f"Error listing film texts: {e}")
            return []

    def get_film_text(self, film_id: int):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM film_text WHERE film_id = %s", (film_id,))
            row = cursor.fetchone()
            cursor.close()
            return FilmText(**row) if row else None
        except Error as e:
            print(f"Error getting film text: {e}")
            return None

    def add_film_text(self, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO film_text (film_id, title) VALUES (%s, %s)",
                (data["film_id"], data["title"])
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error adding film text: {e}")
            return False

    def modify_film_text(self, film_id: int, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE film_text SET title = %s WHERE film_id = %s",
                (data["title"], film_id)
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error modifying film text: {e}")
            return False

    def remove_film_text(self, film_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM film_text WHERE film_id = %s", (film_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error deleting film text: {e}")
            return False
