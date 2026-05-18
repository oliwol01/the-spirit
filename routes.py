from flask import render_template, request
from werkzeug.security import generate_password_hash
from database.queries import create_user, get_all_venues


def init_routes(app):

    @app.route("/")
    def home():


        venues = [
            {
                "name": "Apostolisch Genootschap",
                "type": "Church",
                "image": "img/home/venue-1.png"
            },
            {
                "name": "Apostolisch Genootschap",
                "type": "Church",
                "image": "img/home/venue-1.png"
            },
            {
                "name": "Apostolisch Genootschap",
                "type": "Church",
                "image": "img/home/venue-1.png"
            },
            {
                "name": "Apostolisch Genootschap",
                "type": "Church",
                "image": "img/home/venue-1.png"
            },
            {
                "name": "Apostolisch Genootschap",
                "type": "Church",
                "image": "img/home/venue-1.png"
            },
            {
                "name": "Apostolisch Genootschap",
                "type": "Church",
                "image": "img/home/venue-1.png"
            }
        ]

        return render_template(
            "index.html",
            venues=venues
        )

    @app.route("/login")
    def login():
        return render_template("auth/login.html")

    @app.route("/register")
    def role_selection():
        return render_template("auth/role-selection.html")

    @app.route("/register/form", methods=["GET", "POST"])
    def register():

        role = request.args.get("role")

        if request.method == "POST":

            email = request.form.get("email")
            password = request.form.get("password")

            password_hash = generate_password_hash(password)

            create_user(
                email,
                password_hash,
                role
            )

        return render_template(
            "auth/register.html",
            role=role
        )

    @app.route("/locations")
    def locations():

        venues = [dict(venue) for venue in get_all_venues()]

        return render_template(
            "locations.html",
            venues=venues
        )


    @app.route("/venues/<int:venue_id>")
    def venue(venue_id):

        return render_template(
            "venue.html",
            venue_id=venue_id
        )
