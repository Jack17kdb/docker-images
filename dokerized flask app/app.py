from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Flask REST API running in Docker 🚀"
    })

@app.route('/info', methods=['GET'])
def get_info():
    return jsonify({
        "language": "Python",
        "framework": "Flask",
        "containerized": True
    })

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    if not data or "a" not in data or "b" not in data:
        return jsonify({"error": "Please provide 'a' and 'b' in JSON body"}), 400
    result = data["a"] + data["b"]
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
