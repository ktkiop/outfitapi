import os
import requests

def fetch_taipei_temperature():
    import os
    import requests

    api_key = os.getenv("API_KEY") or "CWA-7B2A9EDB-F7EA-4CF0-86I1-447C600805D2"
    print(f"🛠 使用中的 API_KEY：{api_key}")

    if not api_key:
        raise RuntimeError("💥 沒有拿到 API_KEY，Render 根本沒吃到環境變數")

    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001"
    params = {
        "Authorization": api_key,
        "format": "JSON",
        "StationId": "C0A980"
    }

    print("📡 正在發出請求給氣象局 API...")

    response = requests.get(url, params=params, timeout=5)

    print(f"🔁 API 回應狀態碼：{response.status_code}")
    print(f"📦 API 回傳資料：{response.text[:300]}...")

    data = response.json()
    station_data = data['records']['location'][0]
    temp_str = station_data['weatherElement'][3]['elementValue']
    temp_float = float(temp_str)

    print(f"🌡 取得社子氣溫：{temp_float}°C")

    if temp_float <= 17:
        return (f"{temp_float:.1f}°C", "冷")
    elif temp_float >= 26:
        return (f"{temp_float:.1f}°C", "熱")
    else:
        return (f"{temp_float:.1f}°C", "舒適")
    

# ✅ 本地測試用
if __name__ == "__main__":
    raw_temp, category = fetch_taipei_temperature()
    print("✅ 測試結果：", raw_temp, category)
