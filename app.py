from flask import Flask, request, jsonify
from classifier import classify_style_temp
from recommender import recommend_outfit
from weather import fetch_taipei_temperature
import os

app = Flask(__name__)

@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    text = data.get("text", "")

    style, temp = classify_style_temp(text)
    print(f"🧠 使用者輸入：{text}")
    print(f"🎯 分類結果：風格={style}, 使用者溫度關鍵字={temp}")

    temperature_raw, temp_category = fetch_taipei_temperature()
    temp = temp or temp_category
    print(f"🌡 氣象 API 回傳：{temperature_raw}，分類為：{temp}")

    outfit = recommend_outfit(style, temp)
    print(f"👕 推薦結果：{outfit if outfit else '找不到推薦'}")

    return jsonify({
        "style": style,
        "temperature": temp,
        "temperature_raw": temperature_raw,
        "outfit": outfit,
        "version": "v3"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
