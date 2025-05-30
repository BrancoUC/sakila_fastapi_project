import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.customer import Customer
from typing import List, Optional


class CustomerController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_customers(self) -> List[Customer]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM customer")
            rows = cursor.fetchall()
            return [Customer(**row) for row in rows]
        except Error as e:
            print("Error al listar clientes:", e)
            raise
        finally:
            cursor.close()

    def get_customer(self, customer_id: int) -> Optional[Customer]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM customer WHERE customer_id = %s", (customer_id,))
            row = cursor.fetchone()
            return Customer(**row) if row else None
        except Error as e:
            print("Error al obtener cliente:", e)
            raise
        finally:
            cursor.close()

    def add_customer(self, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """INSERT INTO customer
                   (store_id, first_name, last_name, email, address_id, active, create_date, last_update)
                   VALUES (%s, %s, %s, %s, %s, %s, NOW(), NOW())""",
                (data['store_id'], data['first_name'], data['last_name'], data.get('email'),
                 data['address_id'], data.get('active', 1))
            )
            self.connection.commit()
        except Error as e:
            print("Error al agregar cliente:", e)
            raise
        finally:
            cursor.close()

    def modify_customer(self, customer_id: int, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """UPDATE customer
                   SET store_id = %s, first_name = %s, last_name = %s, email = %s,
                       address_id = %s, active = %s, last_update = NOW()
                   WHERE customer_id = %s""",
                (data['store_id'], data['first_name'], data['last_name'], data.get('email'),
                 data['address_id'], data.get('active', 1), customer_id)
            )
            self.connection.commit()
        except Error as e:
            print("Error al modificar cliente:", e)
            raise
        finally:
            cursor.close()

    def remove_customer(self, customer_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM customer WHERE customer_id = %s", (customer_id,))
            self.connection.commit()
        except Error as e:
            print("Error al eliminar cliente:", e)
            raise
        finally:
            cursor.close()

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
