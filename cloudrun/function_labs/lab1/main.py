from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, world!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

