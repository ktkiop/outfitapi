from flask import Flask, request, jsonify
from classifier import classify_style_temp
from recommender import recommend_outfit

app = Flask(__name__)

@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    sentence = data.get("text", "")
    
    # 分析敘述 → 分類風格＋溫度
    style, temp = classify_style_temp(sentence)

    if not style and not temp:
        return jsonify({"error": "無法判斷風格與溫度"}), 400

    # 根據分類推薦穿搭
    outfit = recommend_outfit(style, temp)
    if outfit:
        return jsonify({
            "style": style,
            "temperature": temp,
            "recommendation": outfit
        })
    else:
        return jsonify({"error": "找不到符合條件的穿搭"}), 404

if __name__ == "__main__":
    app.run(debug=True)
