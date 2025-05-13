from flask import Flask, request, jsonify
import pandas as pd
import random
import requests
from classifier import classify_style_temp
from recommender import recommend_outfit

app = Flask(__name__)

# ==========================
# 🔹 1. 自然語言分類 API
# ==========================
@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    text = data.get("text", "")

    style, temp = classify_style_temp(text)
    print(f"🧠 分類結果：風格={style}, 溫度={temp}")

    outfit = recommend_outfit(style, temp)
    if outfit is None:
        return jsonify({
            "style": style,
            "temperature": temp,
            "recommendation": None
        })

    return jsonify({
        "style": style,
        "temperature": temp,
        "recommendation": outfit
    })

# ==========================
# 🔹 2. 氣溫 API（抓氣象局）
# ==========================
@app.route("/weather", methods=["GET"])
def get_weather():
    location = request.args.get("location", "臺北市")
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": "CWA-7B2A9EDB-F7EA-4CF0-8611-447C600805D2",  
        "format": "JSON",
        "locationName": location,
        "elementName": "MinT,MaxT"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        elements = data["records"]["location"][0]["weatherElement"]
        min_temp = elements[0]["time"][0]["parameter"]["parameterName"]
        max_temp = elements[1]["time"][0]["parameter"]["parameterName"]

        return jsonify({
            "location": location,
            "min_temp": min_temp,
            "max_temp": max_temp
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==========================
# 🔹 Flask app 啟動點
# ==========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
