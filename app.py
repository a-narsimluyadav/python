from flask import Flask

app = Flask(__name__)


@app.get("/")
def hello() -> str:
    return "Hello, Naga lakshmi weeds narsimlu!"


if __name__ == "__main__":
    # Runs on http://127.0.0.1:8000
    app.run(host="127.0.0.1", port=8000, debug=True)


