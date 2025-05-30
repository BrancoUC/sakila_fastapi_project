# controllers/payment_controller.py
import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from datetime import datetime
from entities.payment import Payment, PaymentCreate

class PaymentController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_payments(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM payment")
            rows = cursor.fetchall()
            cursor.close()
            return [Payment(**row) for row in rows]
        except Error as e:
            print(f"Error listing payments: {e}")
            return []

    def get_payment(self, payment_id: int):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM payment WHERE payment_id = %s", (payment_id,))
            row = cursor.fetchone()
            cursor.close()
            return Payment(**row) if row else None
        except Error as e:
            print(f"Error getting payment: {e}")
            return None

    def add_payment(self, data: PaymentCreate):
        try:
            cursor = self.connection.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                "INSERT INTO payment (customer_id, staff_id, rental_id, amount, payment_date, last_update) VALUES (%s, %s, %s, %s, %s, %s)",
                (data.customer_id, data.staff_id, data.rental_id, data.amount, now, now)
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error adding payment: {e}")
            return False

    def modify_payment(self, payment_id: int, data: PaymentCreate):
        try:
            cursor = self.connection.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                "UPDATE payment SET customer_id = %s, staff_id = %s, rental_id = %s, amount = %s, last_update = %s WHERE payment_id = %s",
                (data.customer_id, data.staff_id, data.rental_id, data.amount, now, payment_id)
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error modifying payment: {e}")
            return False

    def remove_payment(self, payment_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM payment WHERE payment_id = %s", (payment_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error deleting payment: {e}")
            return False
