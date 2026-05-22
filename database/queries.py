from database.database import get_db_connection


def create_user(email, password_hash, role):

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users (email, password_hash, role)
        VALUES (?, ?, ?)
        """,
        (email, password_hash, role)
    )

    connection.commit()

    connection.close()


def get_all_venues():

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM venues
        WHERE is_published = 1
        """
    )

    venues = cursor.fetchall()

    connection.close()

    return venues


def get_venue_by_id(venue_id):

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM venues
        WHERE venue_id = ?
        AND is_published = 1
        """,
        (venue_id,)
    )

    venue = cursor.fetchone()

    connection.close()

    return venue