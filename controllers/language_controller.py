# controllers/language_controller.py
import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.language import Language, LanguageCreate
from datetime import datetime

class LanguageController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_languages(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM language")
            rows = cursor.fetchall()
            cursor.close()
            return [Language(**row) for row in rows]
        except Error as e:
            print(f"Error listing languages: {e}")
            return []

    def get_language(self, language_id: int):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM language WHERE language_id = %s", (language_id,))
            row = cursor.fetchone()
            cursor.close()
            return Language(**row) if row else None
        except Error as e:
            print(f"Error retrieving language: {e}")
            return None

    def add_language(self, data: dict):
        try:
            cursor = self.connection.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                "INSERT INTO language (name, last_update) VALUES (%s, %s)",
                (data["name"], now)
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error adding language: {e}")
            return False

    def modify_language(self, language_id: int, data: dict):
        try:
            cursor = self.connection.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                "UPDATE language SET name = %s, last_update = %s WHERE language_id = %s",
                (data["name"], now, language_id)
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error modifying language: {e}")
            return False

    def remove_language(self, language_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM language WHERE language_id = %s", (language_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error deleting language: {e}")
            return False
