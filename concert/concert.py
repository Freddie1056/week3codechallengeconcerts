import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

class Concert:
    def __init__(self, concert_id):
        self.concert_id = concert_id

    def get_band(self):
        query = """
        SELECT b.* FROM bands b
        JOIN concerts c ON b.id = c.band_id
        WHERE c.id = %s
        """
        return self._run_query(query, (self.concert_id,))

    def get_venue(self):
        query = """
        SELECT v.* FROM venues v
        JOIN concerts c ON v.id = c.venue_id
        WHERE c.id = %s
        """
        return self._run_query(query, (self.concert_id,))

    def is_hometown_show(self):
        query = """
        SELECT b.hometown, v.city
        FROM bands b
        JOIN concerts c ON b.id = c.band_id
        JOIN venues v ON c.venue_id = v.id
        WHERE c.id = %s
        """
        result = self._run_query(query, (self.concert_id,))
        return result[0] == result[1]

    def introduction_message(self):
        query = """
        SELECT b.name, b.hometown, v.city
        FROM bands b
        JOIN concerts c ON b.id = c.band_id
        JOIN venues v ON c.venue_id = v.id
        WHERE c.id = %s
        """
        result = self._run_query(query, (self.concert_id,))
        return f"Hello {result[2]}! We are {result[0]} from {result[1]}!"

    def _run_query(self, query, params):
        try:
            with psycopg2.connect(
                dbname=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST')
            ) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    result = cursor.fetchone()
            return result
        except Exception as e:
            print("Query Error:", e)
            return None
