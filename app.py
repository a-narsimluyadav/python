from flask import Flask

app = Flask(__name__)


@app.get("/")
def hello() -> str:
    return "Hello, Naga lakshmi weeds narsimlu!"


if __name__ == "__main__":
    # For local dev / simple runs. In Docker, prefer gunicorn (see Dockerfile).
    app.run(host="0.0.0.0", port=8000, debug=False)


