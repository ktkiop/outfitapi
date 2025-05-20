import csv

def load_outfit_data():
    data = []
    with open("outfit_data.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

data = load_outfit_data()

def recommend_outfit(style, temperature):
    filtered = [row for row in data if row["風格"] == style and row["溫度"] == temperature]
    return filtered
# 這個函式會根據使用者的風格和溫度推薦穿搭
# 它會從 outfit_data.csv 中隨機選擇一套符合條件的穿搭