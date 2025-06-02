import csv
import random
from weather import fetch_taipei_temperature

# 讀取 CSV 資料
with open("outfit_data.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    outfit_data = [dict((k.replace('\ufeff', ''), v) for k, v in row.items()) for row in reader]

# 關鍵字對應風格
style_keywords = {
    "甜酷": ["帥", "甜酷", "個性", "潮"],
    "可愛": ["可愛", "俏皮", "日系", "卡哇伊"],
    "文青": ["文青", "自然", "文藝", "靜謐"],
    "簡約": ["簡約", "極簡", "簡單", "乾淨"],
    "優雅": ["優雅", "氣質", "成熟", "知性"]
}

# 關鍵字對應溫度
temp_keywords = {
    "冷": ["冷", "寒", "發抖"],
    "舒適": ["剛好", "不冷", "不熱", "不冷不熱", "舒適"],
    "熱": ["熱", "流汗", "悶"]
}

def recommend_outfit_by_keyword(text):
    matched_style = ""
    matched_temp = ""

    # ➤ 1. 風格分類
    for style, keywords in style_keywords.items():
        if any(kw in text for kw in keywords):
            matched_style = style
            break
    if not matched_style:
        matched_style = "可愛"  # 預設風格

    # ➤ 2. 溫度分類（使用者輸入 > API 自動分類）
    for temp, keywords in temp_keywords.items():
        if any(kw in text for kw in keywords):
            matched_temp = temp
            print("🧪 用戶輸入指定溫度:", matched_temp)
            break

    # 沒有指定就用 API
    if not matched_temp:
        _, matched_temp = fetch_taipei_temperature()
        print("🧪 使用即時氣溫分類:", matched_temp)

    # ➤ 3. 過濾符合風格 + 溫度的資料
    filtered = [row for row in outfit_data if row["風格"] == matched_style and row["溫度"] == matched_temp]

    print("🧪 推論風格:", matched_style)
    print("🧪 最終溫度分類:", matched_temp)
    print("🧪 符合資料筆數:", len(filtered))

    if not filtered:
        return [], matched_style, matched_temp

    sample_size = min(3, len(filtered))
    result = random.sample(filtered, sample_size)

    return result, matched_style, matched_temp
