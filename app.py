from flask import Flask, request, jsonify
from recommender import recommend_outfit_by_keyword  # 匯入自定義的推薦邏輯函式
from weather import fetch_taipei_temperature         # 匯入抓取台北即時氣溫的函式
from flask_cors import CORS                          # 允許跨來源請求（讓 Flutter 前端可以正常連線）

# 建立 Flask 應用
app = Flask(__name__)
CORS(app)  # 啟用 CORS，允許其他網域（例如 Flutter App）呼叫這個後端

# API 路由：文字輸入分類與推薦（POST）
@app.route("/classify", methods=["POST"])
def classify():
    # 取得從前端送來的 JSON 資料
    data = request.get_json()
    text = data.get("text", "")  # 從中擷取使用者輸入的文字，預設為空字串

    # 呼叫推薦邏輯，傳入文字 → 回傳推薦穿搭、符合的風格、符合的溫度類型
    outfit, matched_style, matched_temp = recommend_outfit_by_keyword(text)

    # 回傳 JSON 結果給前端（包含推薦結果與分析出來的條件）
    return jsonify({
        "style": matched_style,
        "temperature": matched_temp,
        "outfit": outfit
    })

# API 路由：取得即時天氣資訊（GET）
@app.route("/weather", methods=["GET"])
def weather():
    # 呼叫函式取得台北氣溫（字串格式，例如 "27°C（熱）"）
    temp_str = fetch_taipei_temperature()

    # 將結果包裝成 JSON 回傳給前端
    return jsonify({"temperature": temp_str})

# 啟動 Flask 應用，開放外部設備（例如手機）可連線使用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 0.0.0.0 表示對所有 IP 開放，port 設為 5000
