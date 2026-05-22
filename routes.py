from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from database.queries import (
    create_user,
    create_maker,
    create_venue,
    get_all_venues,
    get_venue_by_id,
    get_all_events
)


def init_routes(app):

    @app.route("/")
    def home():

        venues = [dict(venue) for venue in get_all_venues()[:6]]

        events = [dict(event) for event in get_all_events()[:6]]

        return render_template(
            "index.html",
            venues=venues,
            events=events
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

            user_id = create_user(
                email,
                password_hash,
                role
            )

            print(user_id)

            if role == "maker":
                return redirect(
                    url_for(
                        "maker_onboarding",
                        user_id=user_id
                    )
                )

            if role == "venue":
                return redirect(
                    url_for(
                        "venue_onboarding",
                        user_id=user_id
                    )
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

        venue = dict(get_venue_by_id(venue_id))

        events = [dict(event) for event in get_all_events()]

        return render_template(
            "venue.html",
            venue=venue,
            events=events
        )
    @app.route("/proposal-form")
    def proposal_form():
        return render_template("proposal-form.html")
    
    @app.route("/submit-proposal", methods=["POST"])
    def submit_proposal():
        return redirect(url_for("home"))

    @app.route("/maker-onboarding/<int:user_id>", methods=["GET", "POST"])
    def maker_onboarding(user_id):

        if request.method == "POST":

            maker_name = request.form.get("artist_name")

            phone = request.form.get("phone_number")

            gender = request.form.get("gender")

            website = request.form.get("website")

            instagram = request.form.get("instagram")

            linkedin = request.form.get("linkedin")

            tiktok = request.form.get("tiktok")

            program_tags = request.form.getlist("genre")

            program_tags = ",".join(program_tags)

            performances = request.form.get("previous_performances")

            themes = request.form.get("maker_theme")

            create_maker(
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

            return redirect(url_for("home"))

        return render_template(
            "maker-onboarding.html",
            user_id=user_id
        )
    
    @app.route("/venue-onboarding/<int:user_id>", methods=["GET", "POST"])
    def venue_onboarding(user_id):

        if request.method == "POST":

            programming_tags = request.form.getlist("programming_tags")

            programming_tags = ",".join(programming_tags)

            accessibility_features = request.form.getlist("accessibility_features")

            accessibility_features = ",".join(accessibility_features)

            create_venue(
                user_id=user_id,
                name=request.form.get("venue_name"),
                venue_type=request.form.get("venue_type"),
                description=request.form.get("description"),
                phone=request.form.get("phone"),
                website_url=request.form.get("website_url"),
                instagram_url=request.form.get("instagram_url"),
                facebook_url=request.form.get("facebook_url"),
                street_address=request.form.get("street_address"),
                postal_code=request.form.get("postal_code"),
                city=request.form.get("city"),
                programming_tags=programming_tags,
                restrictions=request.form.get("restrictions"),
                capacity=request.form.get("capacity"),
                accessibility_features=accessibility_features,
                price=request.form.get("price"),
                cover_image=None,
                images=None,
                maker_message=request.form.get("maker_message"),
                latitude=None,
                longitude=None
            )

            return redirect(url_for("home"))

        return render_template(
            "venue-onboarding.html",
            user_id=user_id
        )
         
    @app.route("/venue-profile")
    def venue_profile():
        return render_template("venue_profile.html")
    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")
