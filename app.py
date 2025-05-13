from flask import Flask, request, jsonify
import pandas as pd
from classifier import classify_style_temp
from recommender import recommend_outfit
import os

app = Flask(__name__)

@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    text = data.get("text", "")

    style, temp = classify_style_temp(text)

    print(f"🧠 使用者輸入：{text}")
    print(f"🎯 分析結果：風格={style}, 溫度={temp}")

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
