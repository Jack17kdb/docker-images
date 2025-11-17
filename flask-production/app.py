from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Production Flask App Running with Gunicorn!"

if __name__ == "__main__":
    app.run()
