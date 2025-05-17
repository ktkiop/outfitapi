import os
import requests

def fetch_taipei_temperature():
    """
    從中央氣象署 O-A0001-001 服務取得 C0A980（社子）測站的即時氣溫，
    並依據氣溫分類為 冷 / 舒適 / 熱。
    Returns:
        tuple: (溫度字串, 分類字串) or fallback ("無法取得氣溫", "舒適")
    """
    api_key = os.getenv("API_KEY") or "CWA-7B2A9EDB-F7EA-4CF0-86I1-447C600805D2"
    print(f"🛠 使用中的 API_KEY：{api_key}")

    if not api_key:
        print("❌ 沒有從環境變數取得 API_KEY")
        return "無法取得氣溫", "舒適"

    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001"
    params = {
        "Authorization": api_key,
        "format": "JSON",
        "StationId": "C0A980"
    }

    try:
        print("🌐 請求社子測站氣溫資料...")
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        stations = data.get("records", {}).get("Station", [])
        if not stations:
            print("⚠️ 社子站資料為空")
            return "無法取得氣溫", "舒適"

        for station in stations:
            if station.get("StationId") != "C0A980":
                continue

            weather_element = station.get("WeatherElement", {})
            temp = weather_element.get("AirTemperature")

            if temp is None:
                print("⚠️ 社子站無氣溫資料")
                return "無法取得氣溫", "舒適"

            temp_value = float(temp)
            print(f"🌡 社子站即時氣溫：{temp_value:.1f}°C")

            if temp_value < 16:
                return f"{temp_value:.1f}°C", "冷"
            elif temp_value > 26:
                return f"{temp_value:.1f}°C", "熱"
            else:
                return f"{temp_value:.1f}°C", "舒適"

        print("❓ 找不到社子測站資料")
        print("📦 取得回傳資料：", data)
        return "無法取得氣溫", "舒適"

    except Exception as e:
        print(f"❌ 錯誤：{e}")
        return "無法取得氣溫", "舒適"
    

# ✅ 本地測試用
if __name__ == "__main__":
    raw_temp, category = fetch_taipei_temperature()
    print("✅ 測試結果：", raw_temp, category)
