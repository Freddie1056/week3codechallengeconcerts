# Concert Management System

This project offers a system for managing concerts, bands, and venues using PostgreSQL as the database and Python with SQLAlchemy for ORM.

## Project Layout

- **band/**: Includes `band.py` and `__init__.py`. This directory holds the Band class and its associated methods.
- **concert/**: Contains `concert.py`, `__init__.py`, and `__pycache__/`. This folder features the Concert class and related functionalities.
- **venue/**: Comprises `venue.py`, `__init__.py`, and `__pycache__/`. This directory houses the Venue class and its methods.

## Setup Instructions

### Environment Setup

1. **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    ```

2. **Activate the Virtual Environment:**
    - For Windows:
        ```bash
        venv\Scripts\activate
        ```
    - For macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3. **Install Required Packages:**
    ```bash
    pip install psycopg2>=2.9.0 python-dotenv>=0.21.0
    ```

4. **Configure Environment Variables:**

    Create a `.env` file in the root of your project with the following content:

    ```plaintext
    DB_HOST=your_database_host
    DB_NAME=your_database_name
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    ```

    Replace the placeholders with your actual database credentials.

### Running the Application

1. **Verify Database Connection:**
    ```bash
    python -m band.test_connection
    ```

2. **Execute CLI Commands:**
    - To add a new category:
        ```bash
        python cli.py create_category "Electronics"
        ```
    - To add an item:
        ```bash
        python cli.py create_item "Laptop" 1
        ```
    - To list all categories:
        ```bash
        python cli.py read_categories
        ```
    - To list all items:
        ```bash
        python cli.py read_items
        ```
    - To update a category:
        ```bash
        python cli.py update_category 1 "New Name"
        ```
    - To update an item:
        ```bash
        python cli.py update_item 1 "New Item Name"
        ```
    - To remove a category:
        ```bash
        python cli.py delete_category 1
        ```
    - To remove an item:
        ```bash
        python cli.py delete_item 1
        ```

## Class Overview

### Band

- **`Band`**: Handles operations related to bands, including fetching concerts, associated venues, and performance statistics.

### Concert

- **`Concert`**: Manages concert-related operations such as retrieving band details, venue information, and checking if a concert is a hometown show.

### Venue

- **`Venue`**: Oversees venue-related functions such as listing concerts, identifying bands performing frequently, and more.

## Additional Notes

- Ensure that your database configuration is correctly set up and accessible.
- Keep the `.env` file secure and do not share it publicly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
# week3codechallengeconcerts
