import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.store import Store, StoreCreate
from datetime import datetime

class StoreController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_stores(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM store")
            rows = cursor.fetchall()
            cursor.close()
            return [Store(**row) for row in rows]
        except Error as e:
            print(f"Error listing stores: {e}")
            return []

    def get_store(self, store_id: int):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM store WHERE store_id = %s", (store_id,))
            row = cursor.fetchone()
            cursor.close()
            return Store(**row) if row else None
        except Error as e:
            print(f"Error retrieving store: {e}")
            return None

    def add_store(self, data: StoreCreate):
        try:
            cursor = self.connection.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                "INSERT INTO store (manager_staff_id, address_id, last_update) VALUES (%s, %s, %s)",
                (data.manager_staff_id, data.address_id, now)
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error adding store: {e}")
            return False

    def modify_store(self, store_id: int, data: StoreCreate):
        try:
            cursor = self.connection.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                "UPDATE store SET manager_staff_id = %s, address_id = %s, last_update = %s WHERE store_id = %s",
                (data.manager_staff_id, data.address_id, now, store_id)
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error modifying store: {e}")
            return False

    def remove_store(self, store_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM store WHERE store_id = %s", (store_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error deleting store: {e}")
            return False
