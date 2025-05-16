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

    style, temp = classify_style_temp(text)
    print(f"🧠 使用者輸入：{text}")
    print(f"🎯 分析結果：風格={style}, 使用者溫度關鍵字={temp}")

    # ✅ 抓氣溫（社子或台北測站）
    temperature_raw, temp_category = fetch_taipei_temperature()

    # 如果使用者沒指定溫度，就用氣象資料的分類
    temp = temp or temp_category

    outfit = recommend_outfit(style, temp)

    if outfit is None:
        return jsonify({
            "style": style,
            "temperature": temp,
            "temperature_raw": temperature_raw,  # ✅ 必須回傳這個
            "outfit": None
        })

    return jsonify({
        "style": style,
        "temperature": temp,
        "temperature_raw": temperature_raw,  # ✅ 加在這裡
        "outfit": outfit
    })


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
