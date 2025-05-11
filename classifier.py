def classify_style_temp(sentence):
    sentence = sentence.lower()
    style = None
    temp = None

    # 分析風格關鍵字
    if "甜" in sentence or "可愛" in sentence:
        style = "可愛" if "可愛" in sentence else "甜酷"
    elif "酷" in sentence:
        style = "甜酷"
    elif "文青" in sentence or "自然" in sentence:
        style = "文青"
    elif "優雅" in sentence or "氣質" in sentence:
        style = "優雅"
    elif "簡約" in sentence or "極簡" in sentence:
        style = "簡約"

    # 分析溫度關鍵字
    if "冷" in sentence or "怕冷" in sentence:
        temp = "冷"
    elif "不熱" in sentence or "不會熱" in sentence or "不要太熱" in sentence:
        temp = "舒適"
    elif "熱" in sentence:
        temp = "熱"
    elif "剛好" in sentence or "涼爽" in sentence or "舒適" in sentence:
        temp = "舒適"
    
    print(f"🧠 分類結果：風格={style}, 溫度={temp}")
    return style, temp
