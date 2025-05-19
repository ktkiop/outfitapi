from flask import Flask, request, jsonify
from classifier import classify_style_temp
from recommender import recommend_outfit
from weather import fetch_taipei_temperature
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    text = data.get("text", "")

    # 文字分析出風格與溫度（可選）
    style, temp = classify_style_temp(text)
    print(f"使用者輸入：{text}")
    print(f"分析結果：風格 = {style}, 使用者溫度關鍵字 = {temp}")

    # 抓即時氣溫
    temperature_raw, temp_category = fetch_taipei_temperature()
    temp = temp or temp_category

    # 一次推薦多筆穿搭（最多 3 套、避免重複）
    recommendations = []
    used_images = set()

    for _ in range(3):
        outfit = recommend_outfit(style, temp)
        if outfit and outfit["圖片"] not in used_images:
            recommendations.append(outfit)
            used_images.add(outfit["圖片"])

    return jsonify({
        "style": style,
        "temperature": temp,
        "temperature_raw": temperature_raw,
        "outfits": recommendations
    })


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
