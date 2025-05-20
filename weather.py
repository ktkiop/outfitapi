import requests

def fetch_taipei_temperature():
    try:
        print("🌐 從 Open-Meteo 取得台北氣溫...")
        url = "https://api.open-meteo.com/v1/forecast?latitude=25.038&longitude=121.5645&current_weather=true"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        temp = data["current_weather"]["temperature"]
        print(f"🌡 台北即時氣溫：{temp}°C")

        # 回傳 tuple（溫度字串, 溫度分類）
        if temp <= 17:
            return f"{temp:.1f}°C", "冷"
        elif temp >= 26:
            return f"{temp:.1f}°C", "熱"
        else:
            return f"{temp:.1f}°C", "舒適"

    except Exception as e:
        print(f"❌ 錯誤：{e}")
        return "無法取得氣溫", "舒適"
