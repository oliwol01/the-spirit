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

    user_id = cursor.lastrowid

    connection.close()

    return user_id

def get_user_by_email(email):

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()

    connection.close()

    return user

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



def get_all_events():

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM events
        """
    )

    events = cursor.fetchall()

    connection.close()

    return events


def create_maker(
    user_id,
    maker_name,
    phone,
    gender,
    website,
    instagram,
    linkedin,
    tiktok,
    program_tags,
    performances,
    themes
):

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO makers (
            user_id,
            maker_name,
            phone,
            gender,
            website,
            instagram,
            linkedin,
            tiktok,
            program_tags,
            performances,
            themes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            user_id,
            maker_name,
            phone,
            gender,
            website,
            instagram,
            linkedin,
            tiktok,
            program_tags,
            performances,
            themes
        )
    )

    connection.commit()

    connection.close()


def create_venue(
    user_id,
    name,
    venue_type,
    description,
    phone,
    website_url,
    instagram_url,
    facebook_url,
    street_address,
    postal_code,
    city,
    programming_tags,
    restrictions,
    capacity,
    accessibility_features,
    price,
    cover_image,
    images,
    maker_message,
    latitude,
    longitude
):

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO venues (
            user_id,
            name,
            venue_type,
            description,
            phone,
            website_url,
            instagram_url,
            facebook_url,
            street_address,
            postal_code,
            city,
            programming_tags,
            restrictions,
            capacity,
            accessibility_features,
            price,
            cover_image,
            images,
            maker_message,
            latitude,
            longitude
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            user_id,
            name,
            venue_type,
            description,
            phone,
            website_url,
            instagram_url,
            facebook_url,
            street_address,
            postal_code,
            city,
            programming_tags,
            restrictions,
            capacity,
            accessibility_features,
            price,
            cover_image,
            images,
            maker_message,
            latitude,
            longitude
        )
    )

    connection.commit()

    connection.close()