import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.film_actor import FilmActor
from datetime import datetime

class FilmActorController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_film_actors(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM film_actor")
            rows = cursor.fetchall()
            cursor.close()
            return [self._parse_film_actor(row) for row in rows]
        except Error as e:
            print(f"Error listing film_actors: {e}")
            return []

    def get_film_actor(self, film_id: int, actor_id: int):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM film_actor WHERE film_id = %s AND actor_id = %s",
                (film_id, actor_id)
            )
            row = cursor.fetchone()
            cursor.close()
            return self._parse_film_actor(row) if row else None
        except Error as e:
            print(f"Error getting film_actor film_id={film_id} actor_id={actor_id}: {e}")
            return None

    def add_film_actor(self, film_actor_data: dict):
        try:
            cursor = self.connection.cursor()
            now = datetime.now()
            cursor.execute("""
                INSERT INTO film_actor (actor_id, film_id, last_update)
                VALUES (%s, %s, %s)
            """, (
                film_actor_data["actor_id"],
                film_actor_data["film_id"],
                now
            ))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error adding film_actor: {e}")
            return False

    def modify_film_actor(self, film_id: int, actor_id: int, film_actor_data: dict):
        try:
            cursor = self.connection.cursor()
            now = datetime.now()
            cursor.execute("""
                UPDATE film_actor SET last_update = %s
                WHERE film_id = %s AND actor_id = %s
            """, (
                now,
                film_id,
                actor_id
            ))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error modifying film_actor film_id={film_id} actor_id={actor_id}: {e}")
            return False

    def remove_film_actor(self, film_id: int, actor_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "DELETE FROM film_actor WHERE film_id = %s AND actor_id = %s",
                (film_id, actor_id)
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error removing film_actor film_id={film_id} actor_id={actor_id}: {e}")
            return False

    def _parse_film_actor(self, row: dict) -> FilmActor:
        if row is None:
            return None

        # Si last_update viene como datetime, está bien, si no, lo convertimos:
        last_update = row.get("last_update")
        if isinstance(last_update, str):
            try:
                last_update = datetime.fromisoformat(last_update)
            except Exception:
                last_update = None

        row["last_update"] = last_update
        return FilmActor(**row)
