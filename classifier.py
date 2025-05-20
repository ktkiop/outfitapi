import joblib

# 載入模型與轉換器
vectorizer = joblib.load("vectorizer.pkl")

style_model = joblib.load("style_model.pkl")
style_encoder = joblib.load("style_encoder.pkl")

temp_model = joblib.load("temp_model.pkl")
temp_encoder = joblib.load("temp_encoder.pkl")

def classify_style_temp(text):
    vec = vectorizer.transform([text])

    style_idx = style_model.predict(vec)[0]
    temp_idx = temp_model.predict(vec)[0]

    style = style_encoder.inverse_transform([style_idx])[0]
    temp = temp_encoder.inverse_transform([temp_idx])[0]

    return style, temp
# 這個函式會根據使用者的輸入文字分類風格與溫度
# 它會使用之前訓練好的模型來預測風格與溫度