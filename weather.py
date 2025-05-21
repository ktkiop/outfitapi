import requests

def fetch_taipei_temperature():
    """
    從 Open-Meteo API 取得台北市（經緯度固定）的即時氣溫。
    並依據氣溫分類為 冷 / 舒適 / 熱。

    Returns:
        tuple: (溫度字串, 分類字串)
    """

    # 台北市固定經緯度（中正區）
    latitude = 25.0330
    longitude = 121.5654

    # Open-Meteo API URL
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    try:
        # 發送 GET 請求給 Open-Meteo API
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        # 從回傳資料中取得攝氏溫度
        temperature = data.get("current_weather", {}).get("temperature")

        if temperature is None:
            print("無法取得溫度資料")
            return "無法取得氣溫", "舒適"

        # 依照數值分類氣溫
        if temperature < 17:
            category = "冷"
        elif temperature > 26:
            category = "熱"
        else:
            category = "舒適"

        return f"{temperature:.1f}°C", category

    except Exception as e:
        print(f"取得氣溫時發生錯誤: {e}")
        return "無法取得氣溫", "舒適"
