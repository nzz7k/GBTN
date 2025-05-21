from flask import Flask, request, jsonify, send_from_directory
from chat import generate_response

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    reply = generate_response(user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
