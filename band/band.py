import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

class Band:
    def __init__(self, band_id):
        self.band_id = band_id

    def get_concerts(self):
        query = "SELECT * FROM concerts WHERE band_id = %s"
        return self._run_query(query, (self.band_id,))

    def get_venues(self):
        query = """
        SELECT DISTINCT v.* FROM venues v
        JOIN concerts c ON v.id = c.venue_id
        WHERE c.band_id = %s
        """
        return self._run_query(query, (self.band_id,))

    def schedule_concert(self, venue_title, date):
        query = """
        INSERT INTO concerts (band_id, venue_id, date)
        SELECT %s, v.id, %s
        FROM venues v WHERE v.title = %s
        """
        return self._run_query(query, (self.band_id, date, venue_title))

    def band_introductions(self):
        query = """
        SELECT v.city, b.name, b.hometown
        FROM concerts c
        JOIN venues v ON c.venue_id = v.id
        JOIN bands b ON c.band_id = b.id
        WHERE c.band_id = %s
        """
        results = self._run_query(query, (self.band_id,))
        return [f"Hello {r[0]}! We are {r[1]} from {r[2]}!" for r in results]

    def top_performing_band(self):
        query = """
        SELECT b.*, COUNT(c.id) as performance_count
        FROM bands b
        JOIN concerts c ON b.id = c.band_id
        GROUP BY b.id
        ORDER BY performance_count DESC LIMIT 1
        """
        return self._run_query(query, ())

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
