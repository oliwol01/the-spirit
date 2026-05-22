from flask import Flask
from routes import init_routes

app = Flask(__name__)
app.secret_key = "dev-secret-key"

init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)