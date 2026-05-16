from flask import render_template


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