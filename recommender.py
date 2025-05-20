import csv
import random

def load_outfit_data():
    data = []
    with open("outfit_data.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def recommend_outfit(style, temperature):
    data = load_outfit_data()
    filtered = [row for row in data if row["風格"] == style and row["溫度"] == temperature]
    if not filtered:
        return None
    return random.choice(filtered)
