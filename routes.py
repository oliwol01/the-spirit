from flask import render_template
from flask import Flask, render_template, request, redirect, url_for

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

    @app.route("/proposal-form")
    def proposal_form():
        return render_template("proposal-form.html")
    
    @app.route("/submit-proposal", methods=["POST"])
    def submit_proposal():
        return redirect(url_for("home"))

    @app.route("/maker-onboarding")
    def maker_onboarding():

        return render_template(
            "maker-onboarding.html"
        )
    
    @app.route("/venue-onboarding")
    def venue_onboarding():
        return render_template("venue-onboarding.html")
         
    @app.route("/venue-profile")
    def venue_profile():
        return render_template("venue_profile.html")
    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")
