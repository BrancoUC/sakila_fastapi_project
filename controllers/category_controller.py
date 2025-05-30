import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.category import Category
from typing import List, Optional

class CategoryController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise


    def list_categories(self) -> List[Category]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT category_id, name, last_update FROM category")
            rows = cursor.fetchall()
            return [Category(**row) for row in rows]
        except Error as e:
            print("Error al listar categorías:", e)
            raise
        finally:
            cursor.close()

    def get_category(self, category_id: int) -> Optional[Category]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT category_id, name, last_update FROM category WHERE category_id = %s", (category_id,))
            row = cursor.fetchone()
            return Category(**row) if row else None
        except Error as e:
            print("Error al obtener categoría:", e)
            raise
        finally:
            cursor.close()

    def add_category(self, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO category (name, last_update) VALUES (%s, NOW())",
                (data['name'],)
            )
            self.connection.commit()
        except Error as e:
            print("Error al agregar categoría:", e)
            raise
        finally:
            cursor.close()

    def modify_category(self, category_id: int, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE category SET name = %s, last_update = NOW() WHERE category_id = %s",
                (data['name'], category_id)
            )
            self.connection.commit()
        except Error as e:
            print("Error al modificar categoría:", e)
            raise
        finally:
            cursor.close()

    def remove_category(self, category_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM category WHERE category_id = %s", (category_id,))
            self.connection.commit()
        except Error as e:
            print("Error al eliminar categoría:", e)
            raise
        finally:
            cursor.close()

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
