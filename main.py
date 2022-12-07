from flask import Flask, jsonify
import time
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"foo": "bar", "built_at": time.time(), "deployed_at": time.time()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)