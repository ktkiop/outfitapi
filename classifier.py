def classify_style_temp(sentence):
    sentence = sentence.lower()
    style = None
    temp = None

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

    
    if "冷" in sentence or "怕冷" in sentence or "好冷" in sentence:
        temp = "冷"
    elif "熱" in sentence or "悶" in sentence or "流汗" in sentence or "好熱":
        temp = "熱"
    elif "不冷" in sentence or "不熱" in sentence or "剛好" in sentence or "天氣很好":
        temp = "舒適"
    elif "不會熱" in sentence or "不會冷" in sentence or "不會悶" in sentence:
        temp = "舒適"
    elif "天氣好" in sentence or "好天氣" in sentence:
        temp = "舒適"

    return style, temp
