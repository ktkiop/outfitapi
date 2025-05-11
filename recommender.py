import pandas as pd
import numpy as np
import time

df = pd.read_csv("outfit_data.csv", encoding="utf-8")

def recommend_outfit(style, temp):
    filtered = df[(df["風格"] == style) & (df["溫度"] == temp)]

    if filtered.empty:
        return None

    random_seed = int(time.time() * 1000000) % 2**32
    outfit = filtered.sample(n=1, random_state=random_seed).iloc[0]

    return {
        "上衣": outfit["上衣"],
        "下著": outfit["下著"],
        "鞋子": outfit["鞋子"],
        "配件": outfit["配件"],
        "圖片": outfit["圖片"]
    }
