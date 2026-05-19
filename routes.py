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

    @app.route("/maker-onboarding2")
    def maker_onboarding2():

        return render_template(
            "maker-onboarding2.html"
        )
    
    @app.route("/maker-onboarding1")
    def maker_onboarding1():

        return render_template(
            "maker-onboarding1.html"
        )