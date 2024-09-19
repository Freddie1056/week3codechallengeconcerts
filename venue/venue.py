import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

class Venue:
    def __init__(self, venue_id):
        self.venue_id = venue_id

    def get_concerts(self):
        query = "SELECT * FROM concerts WHERE venue_id = %s"
        return self._run_query(query, (self.venue_id,))

    def get_bands(self):
        query = """
        SELECT DISTINCT b.* FROM bands b
        JOIN concerts c ON b.id = c.band_id
        WHERE c.venue_id = %s
        """
        return self._run_query(query, (self.venue_id,))

    def find_concert(self, date):
        query = "SELECT * FROM concerts WHERE venue_id = %s AND date = %s ORDER BY date LIMIT 1"
        return self._run_query(query, (self.venue_id, date))

    def most_common_band(self):
        query = """
        SELECT b.*, COUNT(c.id) as performance_count
        FROM bands b
        JOIN concerts c ON b.id = c.band_id
        WHERE c.venue_id = %s
        GROUP BY b.id
        ORDER BY performance_count DESC LIMIT 1
        """
        return self._run_query(query, (self.venue_id,))

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
                    if query.strip().lower().startswith("select"):
                        result = cursor.fetchall()
                    else:
                        conn.commit()
                        result = None
            return result
        except Exception as e:
            print("Query Error:", e)
            return None
