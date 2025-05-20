import csv
import random

# 從 outfit_data.csv 讀取所有穿搭資料
def load_outfit_data(file_path):
    with open(file_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

# 載入穿搭資料（記得：CSV 檔案應與此檔案在同一層目錄）
outfit_data = load_outfit_data("outfit_data.csv")

# 風格關鍵字對應表
style_keywords = {
    "甜酷": ["帥", "甜酷", "個性", "反差"],
    "可愛": ["可愛", "俏皮", "日系", "卡哇伊"],
    "文青": ["文青", "自然", "文藝", "靜謐"],
    "簡約": ["簡約", "極簡", "簡單", "乾淨"],
    "優雅": ["優雅", "氣質", "成熟", "知性"]
}

# 溫度關鍵字對應表
temp_keywords = {
    "冷": ["冷", "寒", "發抖"],
    "舒適": ["舒適", "不冷不熱", "剛好"],
    "熱": ["熱", "流汗", "悶"]
}

# 根據輸入文字分析關鍵字並推薦穿搭
def recommend_outfit_by_keyword(text):
    matched_style = ""
    matched_temp = ""

    # 嘗試從輸入文字中找出對應風格
    for style, keywords in style_keywords.items():
        if any(kw in text for kw in keywords):
            matched_style = style
            break

    # 嘗試從輸入文字中找出對應溫度
    for temp, keywords in temp_keywords.items():
        if any(kw in text for kw in keywords):
            matched_temp = temp
            break

    # 若沒偵測出來，則給預設值
    if not matched_style:
        matched_style = "甜酷"
    if not matched_temp:
        matched_temp = "熱"

    # 過濾出符合條件的穿搭資料
    filtered = [row for row in outfit_data if row["風格"] == matched_style and row["溫度"] == matched_temp]

    # 如果找不到就傳空
    if not filtered:
        return [], matched_style, matched_temp

    # 隨機選擇一筆資料回傳
    result = random.choice(filtered)
    return [result], matched_style, matched_temp
