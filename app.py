from flask import Flask, request, jsonify
from recommender import recommend_outfit_by_keyword
from weather import fetch_taipei_temperature
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    text = data.get("text", "")

    outfit, matched_style, matched_temp = recommend_outfit_by_keyword(text)

    return jsonify({
        "style": matched_style,
        "temperature": matched_temp,
        "outfit": outfit
    })

@app.route("/weather", methods=["GET"])
def weather():
    temp_str = fetch_taipei_temperature()
    return jsonify({"temperature": temp_str})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
