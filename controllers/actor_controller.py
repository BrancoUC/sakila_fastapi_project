import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.actor import Actor
from typing import List, Optional


class ActorController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_actors(self) -> List[Actor]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT actor_id, first_name, last_name, last_update FROM actor")
            rows = cursor.fetchall()
            return [Actor(**row) for row in rows]
        except Error as e:
            print("Error al listar actores:", e)
            raise
        finally:
            cursor.close()

    def get_actor(self, actor_id: int) -> Optional[Actor]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT actor_id, first_name, last_name, last_update FROM actor WHERE actor_id = %s", (actor_id,))
            row = cursor.fetchone()
            return Actor(**row) if row else None
        except Error as e:
            print("Error al obtener actor:", e)
            raise
        finally:
            cursor.close()

    def add_actor(self, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO actor (first_name, last_name, last_update) VALUES (%s, %s, NOW())",
                (data['first_name'], data['last_name'])
            )
            self.connection.commit()
        except Error as e:
            print("Error al agregar actor:", e)
            raise
        finally:
            cursor.close()

    def modify_actor(self, actor_id: int, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE actor SET first_name = %s, last_name = %s, last_update = NOW() WHERE actor_id = %s",
                (data['first_name'], data['last_name'], actor_id)
            )
            self.connection.commit()
        except Error as e:
            print("Error al modificar actor:", e)
            raise
        finally:
            cursor.close()

    def remove_actor(self, actor_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM actor WHERE actor_id = %s", (actor_id,))
            self.connection.commit()
        except Error as e:
            print("Error al eliminar actor:", e)
            raise
        finally:
            cursor.close()

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
