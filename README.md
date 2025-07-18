# 🛍️ Online Ürün Yorumlarından Duygu Sınıflandırması

Bu proje, e-ticaret sitelerindeki **ürün yorumlarının otomatik olarak olumlu veya olumsuz** olarak sınıflandırılmasını amaçlamaktadır. Türkçe dilinde işlenmiş yorumlar üzerinde **makine öğrenmesi** algoritmaları uygulanarak, kullanıcıya etkileşimli ve görsel açıdan zengin bir analiz ortamı sunulmuştur.

---

## 🎯 Proje Amacı

- E-ticaret platformlarında yapılan yorumları analiz ederek müşteri memnuniyetini otomatik ölçmek  
- Markaların ürün değerlendirme süreçlerine katkı sağlamak  
- Görsel analizlerle veriyi daha anlaşılır ve karar destekleyici hâle getirmek  

---

## 🧰 Kullanılan Teknolojiler

- **Python 3.11**
- **Pandas, NumPy** (veri işleme)
- **Scikit-learn** (makine öğrenmesi modelleri)
- **TF-IDF Vectorizer (1-2 ngram)**
- **MultinomialNB**, **Logistic Regression**, **LinearSVC**
- **Matplotlib, Seaborn, WordCloud** (görselleştirme)
- **NLTK** (Türkçe stopword temizleme)
- **Gradio** (etkileşimli web arayüzü)

---

## 🧠 Uygulanan Adımlar

1. **Veri Temizleme**: Türkçe stopword temizliği ve özel karakter filtreleme
2. **Vektörleştirme**: TF-IDF ile 1-2 n-gram dönüşümü
3. **Model Eğitimi**: MultinomialNB ile temel modelleme
4. **Model Karşılaştırma**: Logistic Regression ve LinearSVC ile doğruluk analizi
5. **Görselleştirme**:
   - Kelime Bulutu
   - Etkili Kelimeler Grafiği
   - Confusion Matrix
   - ROC Eğrisi
   - Model Karşılaştırma Grafiği

---

## 💻 Gradio Arayüz Özellikleri

Arayüz sekmeli yapıdadır:

- 📊 **Performans**: Modelin eğitim ve test doğrulukları ile AUC skorunu gösterir  
- 📉 **Model Karşılaştırması**: Farklı modellerin doğruluk oranlarını grafikle karşılaştırır  
- 🧠 **En Etkili Kelimeler**: MultinomialNB modeline göre sınıflandırmaya en çok etki eden kelimeleri listeler ve görselleştirir  

---

## 📌 Proje Yapısı

```
📦 proje_dosyaları/
├── eticaret-urun-yorumlari.csv
├── main.ipynb
├── model_karsilastirma.png
├── etkili_kelimeler.png
├── README.md
```

---

## 🧪 Örnek Çıktılar

- ✅ Eğitim Doğruluğu: %97.4  
- ✅ Test Doğruluğu: %95.5  
- 📈 AUC Skoru: 0.97  
- 🔠 En etkili kelimeler: `bayıldım`, `rezalet`, `mükemmel`, `bozuk` gibi ifadeler

---

## 🧩 Gereksinimler

Aşağıdaki komut ile gerekli paketleri yükleyebilirsiniz:

```bash
pip install -r requirements.txt
```

Veya:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn nltk gradio wordcloud
```

---

## 🧭 Geliştirme Fikirleri

- SHAP veya LIME ile açıklanabilirlik (modelin neden bu sonucu verdiğini açıklayan grafikler)
- Gerçek zamanlı yorum toplama (web scraping ile)
- Ürün kategorisine göre duygu karşılaştırması
- Kullanıcı yorumu girdisiyle kelime etkisi analizi

---

## 👤 Geliştirici

**Arif Yarencik**  
Bilgisayar Mühendisliği Öğrencisi  
Düzce Üniversitesi  
🔗 [LinkedIn](https://www.linkedin.com/in/arifyarencik)

---

## 📃 Lisans

Bu proje eğitim amaçlıdır ve akademik kullanım için uygundur.
