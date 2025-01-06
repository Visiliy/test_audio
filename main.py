from flask import *
from flask_cors import CORS
from random import randrange

app = Flask(__name__)
CORS(app)

@app.route("/server", methods=["GET"])
def index():
    print("GET")
    return jsonify("GET", 200)

@app.route("/server", methods=["POST"])
def index2():
    content = request.files["audio"].read()
    with open(f"files/audioToSave{randrange(1, 1000000)}.wav", "wb") as fh:
        fh.write(content)
    theAnswer = 'no'
    return jsonify(theAnswer, 200)

if __name__ == "__main__":
    app.run(port=5050) #python main.py