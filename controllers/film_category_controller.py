import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.film_category import FilmCategory

class FilmCategoryController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_film_categories(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM film_category")
            rows = cursor.fetchall()
            cursor.close()
            return [FilmCategory(**row) for row in rows]
        except Error as e:
            print(f"Error listing film categories: {e}")
            return []

    def get_film_category(self, film_id: int, category_id: int):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM film_category WHERE film_id = %s AND category_id = %s",
                (film_id, category_id)
            )
            row = cursor.fetchone()
            cursor.close()
            return FilmCategory(**row) if row else None
        except Error as e:
            print(f"Error getting film category: {e}")
            return None

    def add_film_category(self, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO film_category (film_id, category_id) VALUES (%s, %s)",
                (data["film_id"], data["category_id"])
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error adding film category: {e}")
            return False

    def modify_film_category(self, film_id: int, category_id: int, data: dict):
        
        print("FilmCategory has no modifiable fields apart from PK.")
        return False

    def remove_film_category(self, film_id: int, category_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "DELETE FROM film_category WHERE film_id = %s AND category_id = %s",
                (film_id, category_id)
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error deleting film category: {e}")
            return False
