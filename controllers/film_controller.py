import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.film import Film

class FilmController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_films(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM film")
            rows = cursor.fetchall()
            cursor.close()
            return [self._parse_film(row) for row in rows]
        except Error as e:
            print(f"Error listing films: {e}")
            return []

    def get_film(self, film_id: int):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM film WHERE film_id = %s", (film_id,))
            row = cursor.fetchone()
            cursor.close()
            return self._parse_film(row) if row else None
        except Error as e:
            print(f"Error getting film {film_id}: {e}")
            return None

    def add_film(self, film_data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO film 
                (title, description, release_year, language_id, original_language_id,
                rental_duration, rental_rate, length, replacement_cost, rating, special_features)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                film_data["title"],
                film_data.get("description"),
                film_data.get("release_year"),
                film_data["language_id"],
                film_data.get("original_language_id"),
                film_data["rental_duration"],
                film_data["rental_rate"],
                film_data.get("length"),
                film_data["replacement_cost"],
                film_data.get("rating", "G"),
                ",".join(film_data.get("special_features", [])) if film_data.get("special_features") else None
            ))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error adding film: {e}")
            return False

    def modify_film(self, film_id: int, film_data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE film SET
                title = %s, description = %s, release_year = %s, language_id = %s,
                original_language_id = %s, rental_duration = %s, rental_rate = %s,
                length = %s, replacement_cost = %s, rating = %s, special_features = %s
                WHERE film_id = %s
            """, (
                film_data["title"],
                film_data.get("description"),
                film_data.get("release_year"),
                film_data["language_id"],
                film_data.get("original_language_id"),
                film_data["rental_duration"],
                film_data["rental_rate"],
                film_data.get("length"),
                film_data["replacement_cost"],
                film_data.get("rating", "G"),
                ",".join(film_data.get("special_features", [])) if film_data.get("special_features") else None,
                film_id
            ))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error modifying film {film_id}: {e}")
            return False

    def remove_film(self, film_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM film WHERE film_id = %s", (film_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error removing film {film_id}: {e}")
            return False

    def _parse_film(self, row: dict) -> Film:
        if row is None:
            return None

        special = row.get("special_features")
        if special is None:
            features = []
        elif isinstance(special, str):
            features = [feat.strip() for feat in special.split(",") if feat.strip()]
        elif isinstance(special, (set, list, tuple)):
            features = [str(feat).strip() for feat in special if str(feat).strip()]
        else:
            features = [feat.strip() for feat in str(special).split(",") if feat.strip()]

        row["special_features"] = features
        return Film(**row)
