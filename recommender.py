import csv
import random

# 🔹 載入 CSV 穿搭資料
def load_outfit_data(file_path):
    try:
        with open(file_path, encoding="utf-8-sig") as f:  # 注意：用 utf-8-sig 處理 BOM 問題
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        print("❌ 讀取 CSV 失敗：", e)
        return []

outfit_data = load_outfit_data("outfit_data.csv")

# 🔸 關鍵字對應風格
style_keywords = {
    "甜酷": ["帥", "甜酷", "個性", "潮流", "韓系"],
    "可愛": ["可愛", "俏皮", "日系", "卡哇伊"],
    "文青": ["文青", "自然", "文藝", "靜謐"],
    "簡約": ["簡約", "極簡", "簡單", "乾淨"],
    "優雅": ["優雅", "氣質", "成熟", "知性"]
}

# 🔸 關鍵字對應溫度
temp_keywords = {
    "冷": ["冷", "寒", "發抖"],
    "舒適": ["剛好", "不冷不熱", "舒適"],
    "熱": ["熱", "流汗", "悶"]
}

# 🔹 主推薦邏輯
def recommend_outfit_by_keyword(text):
    matched_style = ""
    matched_temp = ""

    # 🔎 分析輸入文字關鍵字
    for style, keywords in style_keywords.items():
        if any(kw in text for kw in keywords):
            matched_style = style
            break

    for temp, keywords in temp_keywords.items():
        if any(kw in text for kw in keywords):
            matched_temp = temp
            break

    # 若使用者沒輸入明確風格與溫度，給預設值
    if not matched_style:
        matched_style = "甜酷"
    if not matched_temp:
        matched_temp = "熱"

    # ✅ 篩選符合條件的推薦資料
    filtered = [row for row in outfit_data if row["風格"] == matched_style and row["溫度"] == matched_temp]
    if not filtered:
        return [], matched_style, matched_temp

    result = random.choice(filtered)
    return [result], matched_style, matched_temp
