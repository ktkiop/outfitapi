import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
import joblib

# 讀檔
df = pd.read_csv("D:\\outfit_recommender\\flutter_application_1\outfit_api\\ai_train.csv", encoding="utf-8")
# 檢查資料
print(df.head())
print(df.info())
print(df.describe())

# 資料分欄
texts = df["text"].values
styles = df["style"].values
temps = df["temperature"].values

# 向量化文字
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# 風格模型
style_encoder = LabelEncoder()
y_style = style_encoder.fit_transform(styles)

style_model = MultinomialNB()
style_model.fit(X, y_style)

# 溫度模型
temp_encoder = LabelEncoder()
y_temp = temp_encoder.fit_transform(temps)

temp_model = MultinomialNB()
temp_model.fit(X, y_temp)

# 存檔
joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump(style_model, "style_model.pkl")
joblib.dump(style_encoder, "style_encoder.pkl")

joblib.dump(temp_model, "temp_model.pkl")
joblib.dump(temp_encoder, "temp_encoder.pkl")

print("✅ 模型訓練完成並已儲存")
