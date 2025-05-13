from flask import Flask, request, jsonify
import pandas as pd
import requests
from classifier import classify_style_temp
from recommender import recommend_outfit
import os
app = Flask(__name__)

# ==========================
# 🔹 1. 自然語言分類 API
# ==========================
@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    text = data.get("text", "")

    # 🔹 1. 先分類出風格
    style, _ = classify_style_temp(text)
    print(f"🧠 使用者輸入文字：{text}")
    print(f"🎯 偵測風格為：{style}")

    # 🔹 2. 抓氣溫（臺北市）
    try:
        url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
        params = {
            "Authorization": "CWA-7B2A9EDB-F7EA-4CF0-8611-447C600805D2",
            "format": "JSON",
            "locationName": "臺北市",
            "elementName": "MinT,MaxT"
        }
        response = requests.get(url, params=params)
        data = response.json()
        elements = data["records"]["location"][0]["weatherElement"]
        min_temp = int(elements[0]["time"][0]["parameter"]["parameterName"])
        max_temp = int(elements[1]["time"][0]["parameter"]["parameterName"])
        avg_temp = (min_temp + max_temp) / 2
    except Exception as e:
        return jsonify({"error": "無法取得氣溫資料", "details": str(e)}), 500

    # 🔹 3. 溫度分類邏輯
    if avg_temp < 16:
        temp_category = "冷"
    elif avg_temp > 26:
        temp_category = "熱"
    else:
        temp_category = "舒適"

    print(f"🌡️ 臺北市今日溫度：{min_temp}~{max_temp}°C(平均:{avg_temp}°C)")
    print(f"📊 自動判斷溫度分類為：{temp_category}")

    # 🔹 4. 推薦穿搭
    outfit = recommend_outfit(style, temp_category)
    if outfit is None:
        return jsonify({
            "style": style,
            "temperature": temp_category,
            "recommendation": None
        })

    return jsonify({
        "style": style,
        "temperature": temp_category,
        "temperature_raw": f"{min_temp}~{max_temp}°C",
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
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)