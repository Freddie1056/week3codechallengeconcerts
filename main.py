import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def test_connection():
    try:
        with psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST')
        ) as conn:
            print("Database connection successful")
    except Exception as e:
        print("Database connection failed:", e)

from band.band import Band
from venue.venue import Venue
from concert.concert import Concert

def main():
    band_id = 1
    venue_id = 1
    concert_id = 1

    band = Band(band_id)
    print(band.get_concerts())
    print(band.get_venues())
    print(band.band_introductions())
    print(band.top_performing_band())

    
    venue = Venue(venue_id)
    print(venue.get_concerts())
    print(venue.get_bands())
    print(venue.find_concert('2024-09-14'))
    print(venue.most_common_band())

    
    concert = Concert(concert_id)
    print(concert.get_band())
    print(concert.get_venue())
    print(concert.is_hometown_show())
    print(concert.introduction_message())

if __name__ == "__main__":
    test_connection()
    main()
