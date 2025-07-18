import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

turkce_stopwords = set(stopwords.words('turkish'))
def temizle(yorum):
    yorum = str(yorum).lower()
    yorum = re.sub(r"http\S+", "", yorum)
    yorum = re.sub(r"[^a-zçğıöşü0-9\s]", "", yorum)
    yorum = re.sub(r"\s+", " ", yorum).strip()
    yorum = " ".join([w for w in yorum.split() if w not in turkce_stopwords])
    return yorum

def veri_hazirla(dosya):
    df = pd.read_csv(dosya, sep=";")
    df = df[df["Durum"].isin([0, 1])]
    df["temiz_yorum"] = df["Metin"].apply(temizle)
    df = df[df['temiz_yorum'].str.len() > 5]
    return df

def en_sik_kelimeler(df, n=20):
    kelimeler = " ".join(df["temiz_yorum"]).split()
    en_sik = Counter(kelimeler).most_common(n)
    print(f"En sık geçen {n} kelime:")
    for kelime, adet in en_sik:
        print(f"{kelime}: {adet}")

def olumlu_olumsuz_kelimeler(df, n=10):
    olumlu = " ".join(df[df["Durum"]==1]["temiz_yorum"]).split()
    olumsuz = " ".join(df[df["Durum"]==0]["temiz_yorum"]).split()
    print("Olumlu yorumlarda en sık geçen kelimeler:", Counter(olumlu).most_common(n))
    print("Olumsuz yorumlarda en sık geçen kelimeler:", Counter(olumsuz).most_common(n))

def yorum_uzunlugu_hist(df):
    df['yorum_uzunlugu'] = df['temiz_yorum'].apply(len)
    df['yorum_uzunlugu'].hist(bins=50)
    plt.title('Tüm Yorumların Uzunluk Dağılımı')
    plt.xlabel('Karakter Sayısı')
    plt.ylabel('Yorum Sayısı')
    plt.show()

def wordcloud_olustur(df):
    tum_yorumlar = " ".join(df["temiz_yorum"])
    wordcloud = WordCloud(width=800, height=400).generate(tum_yorumlar)
    wordcloud.to_image().show()

def duygu_dagilimi(df):
    df["Durum"].value_counts().plot(kind="bar")
    plt.title("Olumlu/Olumsuz Yorum Dağılımı")
    plt.xlabel("Duygu")
    plt.ylabel("Yorum Sayısı")
    plt.show()

def anahtar_kelime_ara(df, anahtar_kelime):
    bulunanlar = df[df["temiz_yorum"].str.contains(anahtar_kelime)]
    print(f"'{anahtar_kelime}' kelimesi geçen yorum sayısı:", len(bulunanlar))
    print(bulunanlar[["temiz_yorum", "Durum"]].head())

def model_egit_tahmin(df):
    X_train, X_test, y_train, y_test = train_test_split(
        df['temiz_yorum'], df['Durum'], test_size=0.2, random_state=42)
    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    model = MultinomialNB()
    model.fit(X_train_vec, y_train)
    y_pred = model.predict(X_test_vec)
    print('Doğruluk:', accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    # Tüm veri için tahmin
    df["tahmin"] = model.predict(vectorizer.transform(df["temiz_yorum"]))
    print(df[["temiz_yorum", "Durum", "tahmin"]].head())
    return model, vectorizer

def main():
    df = veri_hazirla("PROJEE/eticaret-urun-yorumlari.csv")
    print(df.head())
    print(df.columns)
    print(df.shape)
    print(df.isnull().sum())
    print(df["Durum"].value_counts())
    en_sik_kelimeler(df)
    olumlu_olumsuz_kelimeler(df)
    yorum_uzunlugu_hist(df)
    wordcloud_olustur(df)
    duygu_dagilimi(df)
    anahtar_kelime = input("Aramak istediğiniz anahtar kelime: ")
    anahtar_kelime_ara(df, anahtar_kelime)
    model, vectorizer = model_egit_tahmin(df)

if __name__ == "__main__":
    main()
