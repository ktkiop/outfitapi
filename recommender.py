import csv
import random

# 讀取 outfit_data.csv 並載入為列表

def load_outfit_data(file_path):
    """
    從 CSV 檔案中讀取穿搭資料
    Args:
        file_path (str): 檔案路徑
    Returns:
        List[Dict]: 每筆資料都是字典
    """
    with open(file_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

# ✅ 載入資料
outfit_data = load_outfit_data("outfit_data.csv")

# 關鍵字與風格對應表
style_keywords = {
    "甜酷": ["帥", "甜酷", "個性", "反差"],
    "可愛": ["可愛", "俏皮", "日系", "卡哇伊"],
    "文青": ["文青", "自然", "文藝", "靜謐"],
    "簡約": ["簡約", "極簡", "簡單", "乾淨"],
    "優雅": ["優雅", "氣質", "成熟", "知性"]
}

temp_keywords = {
    "冷": ["冷", "寒", "發抖"],
    "舒適": ["舒適", "剛好", "不冷不熱"],
    "熱": ["熱", "流汗", "悶"]
}

def recommend_outfit_by_keyword(text):
    """
    根據文字分析推薦穿搭
    Args:
        text (str): 使用者輸入文字
    Returns:
        Tuple: (推薦資料 list, 判定風格 str, 判定溫度 str)
    """
    matched_style = ""
    matched_temp = ""

    # 分析風格
    for style, keywords in style_keywords.items():
        if any(kw in text for kw in keywords):
            matched_style = style
            break

    # 分析溫度
    for temp, keywords in temp_keywords.items():
        if any(kw in text for kw in keywords):
            matched_temp = temp
            break

    # 預設值（沒偵測到時）
    if not matched_style:
        matched_style = "甜酷"
    if not matched_temp:
        matched_temp = "熱"

    # 篩選資料
    filtered = [row for row in outfit_data if row["風格"] == matched_style and row["溫度"] == matched_temp]

    if not filtered:
        return [], matched_style, matched_temp

    result = random.choice(filtered)
    return [result], matched_style, matched_temp
