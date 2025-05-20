import csv
import random

def load_outfit_data():
    data = []
    with open("outfit_data.csv", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

outfit_data = load_outfit_data()
# 關鍵字對應到風格分類（依你定義的風格）
style_keywords = {
    "甜酷": ["帥", "甜酷", "個性", "反差"],
    "可愛": ["可愛", "俏皮", "日系", "卡哇伊"],
    "文青": ["文青", "自然", "文藝", "靜謐"],
    "簡約": ["簡約", "極簡", "簡單", "乾淨"],
    "優雅": ["優雅", "氣質", "成熟", "知性"]
}

# 關鍵字對應溫度分類（冷／舒適／熱）
temp_keywords = {
    "冷": ["冷", "寒", "發抖"],
    "舒適": ["剛好", "不冷不熱", "舒適"],
    "熱": ["熱", "流汗", "悶"]
}

# 從 CSV 檔案讀入穿搭資料
with open("outfit_data.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    outfit_data = list(reader)

# 根據關鍵字文字找出風格與溫度，並回傳一筆推薦
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

    # 如果沒偵測出風格或溫度，就預設一組
    if not matched_style:
        matched_style = "甜酷"
    if not matched_temp:
        matched_temp = "熱"

    # 篩選出符合的資料後，隨機挑 1 筆
    filtered = [row for row in outfit_data if row["風格"] == matched_style and row["溫度"] == matched_temp]
    if not filtered:
        return [], matched_style, matched_temp

    result = random.choice(filtered)
    return [result], matched_style, matched_temp