import requests

def fetch_taipei_temperature():
    url = (
        "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
        "?Authorization=CWA-7B2A9EDB-F7EA-4CF0-8611-447C600805D2"
        "&format=JSON"
        "&locationName=臺北市"
        "&elementName=MinT,MaxT"
    )

    try:
        res = requests.get(url, timeout=5)
        data = res.json()
        elements = data["records"]["location"][0]["weatherElement"]

        min_temp = int(elements[0]["time"][0]["parameter"]["parameterName"])
        max_temp = int(elements[1]["time"][0]["parameter"]["parameterName"])
        avg = (min_temp + max_temp) / 2

        if avg < 16:
            category = "冷"
        elif avg > 26:
            category = "熱"
        else:
            category = "舒適"

        return f"{min_temp}~{max_temp}°C", category

    except Exception as e:
        print(f"❌ 氣象 API 錯誤：{e}")
        return "無法取得氣溫", "舒適"
