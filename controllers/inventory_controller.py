import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.inventory import Inventory
from datetime import datetime

class InventoryController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_inventories(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM inventory")
            rows = cursor.fetchall()
            cursor.close()
            return [Inventory(**row) for row in rows]
        except Error as e:
            print(f"Error listing inventories: {e}")
            return []

    def get_inventory(self, inventory_id: int):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM inventory WHERE inventory_id = %s", (inventory_id,))
            row = cursor.fetchone()
            cursor.close()
            return Inventory(**row) if row else None
        except Error as e:
            print(f"Error getting inventory: {e}")
            return None

    def add_inventory(self, data: dict):
        try:
            cursor = self.connection.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                "INSERT INTO inventory (film_id, store_id, last_update) VALUES (%s, %s, %s)",
                (data["film_id"], data["store_id"], now)
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error adding inventory: {e}")
            return False

    def modify_inventory(self, inventory_id: int, data: dict):
        try:
            cursor = self.connection.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                "UPDATE inventory SET film_id = %s, store_id = %s, last_update = %s WHERE inventory_id = %s",
                (data["film_id"], data["store_id"], now, inventory_id)
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error modifying inventory: {e}")
            return False

    def remove_inventory(self, inventory_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM inventory WHERE inventory_id = %s", (inventory_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error deleting inventory: {e}")
            return False
