import csv
import random

# 讀取 CSV 檔案中的穿搭資料
with open("outfit_data.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    outfit_data = [dict((k.replace('\ufeff', ''), v) for k, v in row.items()) for row in reader]
    outfit_data = list(reader)

# 關鍵字對應到風格分類
style_keywords = {
    "甜酷": ["帥", "甜酷", "個性", "潮"],
    "可愛": ["可愛", "俏皮", "日系", "卡哇伊"],
    "文青": ["文青", "自然", "文藝", "靜謐"],
    "簡約": ["簡約", "極簡", "簡單", "乾淨"],
    "優雅": ["優雅", "氣質", "成熟", "知性"]
}

# 關鍵字對應到溫度分類
temp_keywords = {
    "冷": ["冷", "寒", "發抖"],
    "舒適": ["剛好", "不冷不熱", "舒適"],
    "熱": ["熱", "流汗", "悶"]
}

def recommend_outfit_by_keyword(text):
    matched_style = ""
    matched_temp = ""

    for style, keywords in style_keywords.items():
        if any(kw in text for kw in keywords):
            matched_style = style
            break

    for temp, keywords in temp_keywords.items():
        if any(kw in text for kw in keywords):
            matched_temp = temp
            break

    # 預設值
    if not matched_style:
        matched_style = "甜酷"
    if not matched_temp:
        matched_temp = "熱"

    # 過濾符合條件的資料
    filtered = [row for row in outfit_data if row["風格"] == matched_style and row["溫度"] == matched_temp]
    if not filtered:
        return [], matched_style, matched_temp

    # 從中隨機抽取最多三筆不重複資料
    sample_size = min(3, len(filtered))
    result = random.sample(filtered, sample_size)

    return result, matched_style, matched_temp
