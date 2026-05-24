from flask import render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from database.queries import (
    create_user,
    create_maker,
    create_venue,
    get_all_venues,
    get_venue_by_id,
    get_venue_by_user_id,
    get_all_events,
    get_user_by_email,
    create_proposal,
    get_maker_by_user_id,
    get_proposals_by_venue_id,
    get_proposals_by_maker_id
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

    @app.route("/login", methods=["GET", "POST"])
    def login():

        error = None
        email = ""

        if request.method == "POST":

            email = request.form.get("email", "")
            password = request.form.get("password", "")

            user = get_user_by_email(email)

            if user and check_password_hash(
                user["password_hash"],
                password
            ):

                session["user_id"] = user["user_id"]
                session["role"] = user["role"]

                return redirect(url_for("dashboard"))

            error = "Invalid email or password. Please try again."

        return render_template(
            "auth/login.html",
            error=error,
            email=email
        )

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

            session["user_id"] = user_id
            session["role"] = role

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
    @app.route("/proposal-form/<int:venue_id>")
    def proposal_form(venue_id):

        if not session.get("user_id"):
            return redirect(url_for("login"))

        session["proposal_venue_id"] = venue_id

        return render_template(
            "proposal-form.html",
            venue_id=venue_id
        )
    
    @app.route("/submit-proposal", methods=["POST"])
    def submit_proposal():

        if not session.get("user_id"):
            return redirect(url_for("login"))

        user_id = session.get("user_id")

        maker = get_maker_by_user_id(user_id)

        if not maker:
            return redirect(url_for("dashboard"))

        maker_id = maker["maker_id"]

        venue_id = request.form.get("venue_id")

        if not venue_id:
            venue_id = session.get("proposal_venue_id")

        if not venue_id:
            return redirect(url_for("locations"))

        format_tags = request.form.getlist("format_tags")
        format_tags = ",".join(format_tags)

        collaboration_style = request.form.getlist("collaboration_style")
        collaboration_style = ",".join(collaboration_style)

        create_proposal(
            maker_id=maker_id,
            venue_id=venue_id,
            title=request.form.get("title"),
            core_idea=request.form.get("core_idea"),
            format_tags=format_tags,
            venue_fit=request.form.get("venue_fit"),
            collaboration_style=collaboration_style,
            additional_details=request.form.get("additional_details"),
            event_experience=request.form.get("event_experience"),
            audience_takeaway=request.form.get("audience_takeaway"),
            audience_size=request.form.get("audience_size"),
            technical_requirements=request.form.get("technical_requirements")
        )

        session.pop("proposal_venue_id", None)

        return redirect(url_for("dashboard"))

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

            session["user_id"] = user_id
            session["role"] = "maker"

            return redirect(url_for("dashboard"))

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

            session["user_id"] = user_id
            session["role"] = "venue"

            return redirect(url_for("dashboard"))

        return render_template(
            "venue-onboarding.html",
            user_id=user_id
        )
         
    @app.route("/venue-profile")
    def venue_profile():
        return render_template("venue_profile.html")
    @app.route("/logout")
    def logout():

        session.clear()

        return redirect(url_for("home"))
    @app.route("/dashboard")
    def dashboard():

        if not session.get("user_id"):
            return redirect(url_for("login"))

        role = session.get("role")

        display_name = "User"
        venue = None

        if role == "maker":

            maker = get_maker_by_user_id(session.get("user_id"))

            if maker:
                display_name = maker["maker_name"]

        elif role == "venue":

            venue = get_venue_by_user_id(session.get("user_id"))

            if venue:
                display_name = venue["name"]

        return render_template(
            "dashboard.html",
            role=role,
            display_name=display_name,
            venue=venue
        )

    @app.route("/inbox")
    def inbox():

        if not session.get("user_id"):
            return redirect(url_for("login"))

        role = session.get("role")

        proposals = []

        if role == "venue":

            venue = get_venue_by_user_id(session.get("user_id"))

            if not venue:
                return redirect(url_for("dashboard"))

            proposals = get_proposals_by_venue_id(venue["venue_id"])

        elif role == "maker":

            maker = get_maker_by_user_id(session.get("user_id"))

            if not maker:
                return redirect(url_for("dashboard"))

            proposals = get_proposals_by_maker_id(maker["maker_id"])

        else:
            return redirect(url_for("dashboard"))

        return render_template(
            "inbox.html",
            proposals=proposals,
            role=role
        )

    @app.route("/proposal-info/<int:venue_id>")
    def proposal_info(venue_id):

        venue = get_venue_by_id(venue_id)

        return render_template(
            "proposal-info.html",
            venue=venue,
            venue_id=venue_id
        )