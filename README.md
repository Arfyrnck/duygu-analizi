# 🛍️ Online Ürün Yorumlarından Duygu Sınıflandırması

Bu proje, Türkçe e-ticaret yorumlarını kullanarak **duygu analizi (sentiment analysis)** gerçekleştirmeyi amaçlar. Kullanıcı yorumları makine öğrenmesi modelleriyle analiz edilerek **olumlu** veya **olumsuz** olarak sınıflandırılır.

> 💡 Proje; geliştirme, görselleştirme ve açıklanabilirlik odaklıdır. Gradio tabanlı kullanıcı dostu bir arayüz ile tamamlanmıştır.

---

## 📁 Proje Klasör Yapısı
e-ticaret-duygu-analizi/
│
├── eticaret-urun-yorumlari.xlsx     # Veri seti
├── kod_dosyasi.ipynb                # Tüm kodları içeren Jupyter Notebook
├── README.md                        # Proje açıklama dosyası
├── model_karsilastirma.png         # Model karşılaştırma görseli
├── etkili_kelimeler.png            # Tahmine etki eden kelimeler grafiği
├── output (1).png                  # ROC eğrisi görseli
├── Online Ürün Yorumlarından ….pptx  # PowerPoint sunumu
├── .gradio/                         # Gradio ile oluşturulan içerikler
└── gradio_arayuz.py                # Gradio arayüz betiği (opsiyonel)

---

## 🎯 Proje Amacı

- Türkçe e-ticaret yorumlarında duygu sınıflandırması yapmak  
- TF-IDF, Naive Bayes ve Logistic Regression gibi algoritmalar ile karşılaştırma  
- Kullanıcı dostu, sezgisel ve görsel yönü güçlü bir Gradio arayüzü oluşturmak

---

## ⚙️ Kullanılan Yöntemler

- 🔡 **Veri Ön İşleme:** Küçük harfe çevirme, noktalama işaretlerinin temizlenmesi, stopword filtreleme  
- 📈 **Vektörleştirme:** TF-IDF (min_df, max_df, n-gram ayarlı)  
- 🧠 **Modeller:**
  - `Multinomial Naive Bayes (alpha=0.5)`
  - `Logistic Regression (class_weight='balanced')`
- 🧪 **Değerlendirme:**
  - Confusion Matrix
  - ROC Curve ve AUC Skoru
  - 5-fold Cross Validation
- 📊 **Görselleştirmeler:**
  - Kelime Bulutu
  - Öne çıkan kelimeler grafiği
  - Model karşılaştırma bar grafiği

---

## 📊 Performans Göstergeleri

| Ölçüt                  | Değer     |
|------------------------|-----------|
| 🎯 Doğruluk (Test)     | **%95.2** |
| 📈 AUC Skoru           | **0.989** |
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

## ⚖️ Model Karşılaştırması

| Model                | Eğitim Doğruluğu | Test Doğruluğu |
|---------------------|------------------|----------------|
| Logistic Regression | %97.44           | %94.97         |
| Multinomial NB      | %97.40           | %95.56         |
| Linear SVC          | %99.48           | %95.52         |

> 🔍 **MultinomialNB**, özellikle AUC skoru ve test doğruluğu bakımından öne çıkmaktadır.

---

## 🖥️ Gradio Arayüz Özellikleri

Gradio ile çok sekmeli, sade ve kullanıcı odaklı bir arayüz geliştirildi:

- 🛍️ **Tahmin Sekmesi:** Girilen yoruma göre anında duygu tahmini  
- 📊 **Performans Sekmesi:** Eğitim / test skorları ve AUC değeri  
- 📈 **Model Karşılaştırması:** Grafiksel doğruluk karşılaştırması  
- 🔠 **En Etkili Kelimeler:** Kelimelerin model kararına etkilerinin görselleştirilmesi  

---

## 🔧 Kurulum

```bash
pip install gradio scikit-learn matplotlib pandas
python gradio_arayuz.py

🎓 Sunum Dosyası

PowerPoint sunumu da projeye dahildir:
📄 Online Ürün Yorumlarından Duygu Sınıflandırması.pptx

⸻

👤 Geliştirici

Arif Yarencik
Bilgisayar Mühendisliği Öğrencisi
Düzce Üniversitesi
🔗 LinkedIn Profilim

⸻

📄 Lisans

Bu proje yalnızca eğitim ve akademik kullanım amaçlıdır.