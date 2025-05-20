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

    # 預測風格（溫度先忽略）
    style, _ = classify_style_temp(text)

    # 取得即時天氣（第二個回傳值是分類結果：冷 / 舒適 / 熱）
    _, temp = fetch_taipei_temperature()

    # 若使用者說太熱 → 調高溫度分類
    if any(kw in text for kw in ["太熱", "熱死", "悶", "中暑"]):
        if temp == "冷":
            temp = "舒適"
        elif temp == "舒適":
            temp = "熱"

    # 若使用者說太冷 → 調低溫度分類
    elif any(kw in text for kw in ["太冷", "冷死", "冷爆", "發抖"]):
        if temp == "熱":
            temp = "舒適"
        elif temp == "舒適":
            temp = "冷"

    # 推薦穿搭
    outfit = recommend_outfit(style, temp)

    return jsonify({
        "style": style,
        "temperature": temp,
        "outfit": outfit
    })

if __name__ == "__main__":
    app.run(debug=True)
