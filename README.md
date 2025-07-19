# 🛍️ Online Ürün Yorumlarından Duygu Sınıflandırması

Bu proje, Türkçe e-ticaret yorumlarını kullanarak **duygu analizi** (sentiment analysis) gerçekleştirmeyi amaçlar. Kullanıcı yorumları makine öğrenmesi modelleriyle işlenir ve **olumlu** veya **olumsuz** olarak sınıflandırılır.

> 💡 Geliştirme, görselleştirme ve açıklanabilirlik odaklıdır. Gradio tabanlı kullanıcı dostu bir arayüz ile tamamlandı.

---

## 📁 Proje Klasör Yapısı

📦 e-ticaret-duygu-analizi
├── eticaret-urun-yorumlari.xlsx # Veri seti
├── kod dosyası.ipynb # Tüm kodları içeren Jupyter Notebook
├── README.md # Proje açıklama dosyası
├── model_karsilastirma.png # Model karşılaştırma görseli
├── etkili_kelimeler.png # Tahmine etki eden kelimeler grafiği
├── output (1).png # ROC eğrisi görseli
├── Online Ürün Yorumlarından ...pptx # Sunum dosyası
├── .gradio/ # Gradio ile oluşturulan içerikler
└── gradio_arayuz.py # Gradio arayüz betiği (opsiyonel)

yaml
Kopyala
Düzenle

---

## 🎯 Proje Amacı

- E-ticaret yorumlarının analizini yaparak duygu sınıflandırması gerçekleştirmek  
- TF-IDF, Naive Bayes ve Logistic Regression gibi algoritmalarla kıyaslama  
- Kullanıcı dostu ve görsel açıdan zengin bir Gradio arayüzü sunmak  

---

## ⚙️ Kullanılan Yöntemler

- 🔡 **Veri Temizleme & Ön İşleme:** Noktalama, küçük harfe çevirme, stopword temizleme  
- 📈 **Vektörleştirme:** Gelişmiş TF-IDF (min_df, max_df, n-gram optimizasyonlu)  
- 🧠 **Makine Öğrenmesi Modelleri:**
  - `Multinomial Naive Bayes (alpha=0.5)`
  - `Logistic Regression (class_weight='balanced')`
- 📊 **Değerlendirme Ölçütleri:**
  - Confusion Matrix
  - ROC Curve ve AUC Skoru
  - 5-fold Cross Validation
- 📷 **Görselleştirmeler:**
  - Kelime Bulutu
  - Etkili Kelimeler Grafiği
  - Model Karşılaştırma Bar Chart

---

## 📊 Performans Göstergeleri

| Ölçüt                  | Değer      |
|------------------------|------------|
| 🎯 Doğruluk (Test)     | **%95.2**  |
| 📈 AUC Skoru           | **0.989**  |
| 🔁 CV Ortalama Skoru   | **0.9498** |

---

## 🧠 Confusion Matrix – MultinomialNB

![Confusion Matrix](model_karsilastirma.png)

---

## 🚀 ROC Eğrisi

![ROC Curve](output%20(1).png)

---

## 🧾 Tahmine En Çok Etki Eden Kelimeler

![Etkili Kelimeler](etkili_kelimeler.png)

---

## 🧪 Model Karşılaştırması

| Model                | Eğitim Doğruluğu | Test Doğruluğu |
|---------------------|------------------|----------------|
| Logistic Regression | %97.44           | %94.97         |
| Multinomial NB      | %97.40           | %95.56         |
| Linear SVC          | %99.48           | %95.52         |

> 🔍 **MultinomialNB**, özellikle AUC skoru ve test doğruluğu bakımından öne çıkmıştır.

---

## 🖥️ Gradio Arayüzü Özellikleri

Proje sonunda Gradio ile sade, sezgisel ve çok sekmeli bir web arayüz tasarlandı:

- 🛍️ **Tahmin Sekmesi:** Kullanıcıdan gelen yoruma göre anında duygu tahmini
- 📊 **Performans Sekmesi:** Eğitim & test doğruluğu, AUC skoru
- 📈 **Model Karşılaştırması:** Grafiksel doğruluk karşılaştırması
- 🔠 **En Etkili Kelimeler:** Tahmin kararlarını etkileyen en önemli kelimelerin görselleştirilmesi

### 🔧 Kurulum

```bash
pip install gradio scikit-learn matplotlib pandas
python gradio_arayuz.py
🎓 Sunum Dosyası
🎤 PowerPoint sunumu da projeye dahildir:

Online Ürün Yorumlarından Duygu Sınıflandırması.pptx

---

## 👤 Geliştirici

**Arif Yarencik**  
Bilgisayar Mühendisliği Öğrencisi  
Düzce Üniversitesi  
🔗 [LinkedIn](https://www.linkedin.com/in/arifyarencik)

---

## 📃 Lisans

Bu proje eğitim amaçlıdır ve akademik kullanım için uygundur.
