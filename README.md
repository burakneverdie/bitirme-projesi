# 💬 Doğal Dil İşleme Teknikleri ile Duygu Analizi

Bu proje, **kullanıcı tarafından girilen bir URL içerisindeki metinleri veya kullanıcı tarafından girilen metinleri analiz ederek duygu tahmini yapan** bir Python projesidir. Önceden eğitilmiş model ile yeni girilen metinler üzerinde tahminler gerçekleştirmektedir.

---

## 📊 Özellikler

* Uygulamanın **GUI** ve **CLI** olmak üzere iki farklı versiyonu vardır.
* **GUI versiyonu:** Verilen URL üzerinden web scraping yöntemi ile metinleri elde eder ve bu metinler üzerinde duygu analizi yaparak olasılıkları belirler.
* **CLI versiyonu:** Kullanıcı tarafından girilen metin üzerinde duygu analizi yapar ve belirlenen etiketi (pozitif, negatif veya nötr) çıktı olarak verir.

Ayrıca proje geliştirme sürecinde farklı algoritmalar ile doğruluk sonuçları test edilmiştir; örn. (Naive Bayes, Random Forest, Support Vector Machine) ve test edilen algoritmalar `deneme` klasörünün içerisinde mevcuttur.

---

## ⚙️ Kurulum

1. Projeyi klonlayın veya indirin:

   ```bash
   git clone https://github.com/burakneverdie/bitirme-projesi.git
   cd bitirme-projesi
   ```

2. Veri seti için rar dosyası içerisindeki datasets klasörünü çıkartın ve bitirme-projesi klasörünün ana dizinine atın.

3. Gerekli kütüphaneleri yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

4. Eğer yoksa NLTK paketlerini indirmeniz gerekebilir:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

---

## ▶️ Kullanım

### GUI Versiyonu

```bash
python calisma.py
```

* Arayüzde URL kısmına bir URL girin ve "Analiz Et" butonuna tıklayın.
* Model, alınan metinler üzerinde analiz gerçekleştirdikten sonra olasılıkları arayüzde ekrana yansıtacaktır.

### CLI Versiyonu

* `deneme` klasöründeki `m2.py` dosyasını çalıştırın ve bir metin girin.
* Model, tahmin edilen duyguyu ekranda çıktı olarak gösterecektir.

> Test için kullanılan algoritmalar ve modeller `deneme` klasörünün içerisindedir.

---

## 🤖 Çalışma Mantığı

### Model ve Tokenizer Yükleme
- Daha önce eğitilmiş duygu analizi modeli ve tokenizer yüklenir.
- Tokenizer, metindeki kelimeleri sayısal verilere (indeksler) dönüştürmek için kullanılır.

### Metin Ön İşleme
- Yorumlar küçük harfe çevrilir, özel karakterler temizlenir, kelimeler tokenize edilir ve gereksiz kelimeler (stopwords) çıkarılır.

### Metinlerin Sayısal Formata Dönüştürülmesi
- Ön işleme yapılan kelimeler, tokenizer kullanılarak sayı dizilerine (sequence) dönüştürülür.
- Bu sayısal diziler, modelin anlayacağı formata getirilmek için `pad_sequences` ile aynı uzunluğa getirilir.

### Web Sitesinden Veri Çekme
- Girilen URL’den metinler toplanır.

### Duygu Analizi
- Model, her sayısal dizi girdi için tahmin yapar ve sonucu Negatif, Nötr veya Pozitif olarak sınıflandırır.
- Her sınıf için olasılık yüzdeleri hesaplanır.

### Sonuçların Gösterimi ve Kaydedilmesi
- Analiz edilen yorumlar ve tahminler ekranda listelenir.
- Çıkan sonuç `comments.txt` dosyasına kaydedilir.

---

## 🛠 Kullanılan Teknolojiler

* **Python 3** – Programlama dili
* **Tkinter** – Grafiksel kullanıcı arayüzü (GUI)
* **Pillow (PIL)** – Görselleri işleme ve gösterme
* **Requests** – Web sitelerinden veri çekme
* **BeautifulSoup4** – HTML verilerini parse etme
* **TensorFlow / Keras** – Makine öğrenmesi ve duygu analizi modeli
* **NumPy** – Sayısal işlemler ve olasılık hesaplamaları
* **NLTK** – Doğal dil işleme, tokenizasyon ve stopwords
* **scikit-learn** – Metin vektörleştirme, modelleme ve değerlendirme (Logistic Regression, Tfidf)
* **Pandas** – Veri işleme ve yönetimi
* **Seaborn / Matplotlib** – Grafik ve görselleştirme

---

## 📌 Ek Bilgiler

### 1. Dosya Yolları
Kodda `background_path`, `model_path` ve `tokenizer_path` mutlak yol (absolute path) ile verilmiştir. Kullanıcıların kendi sistemine göre bu yolları değiştirmesi gerekir veya göreli yollar kullanmaları önerilir.

**Örnek:**
```python
background_path = "./bitirme/yapayzekaresmi.jpg"
model_path = "./model/sentiment_model.keras"
tokenizer_path = "./bitirme/tokenizer.pickle"
```

### 2. Web Scraping Sınırlamaları
Kod sadece `<p>` etiketlerini çekmektedir. Bu nedenle:
- Bazı web sitelerinde metinler `<p>` dışında başka etiketlerde olabilir, tüm metinler çekilmeyebilir.
- Bazı siteler scraping işlemlerine izin vermeyebilir veya engelleyebilir.

** ❗ Not:** Web scraping işlemleri sırasında site politikalarına dikkat edin.

### 3. Eğitilmiş Model
Eğitilmiş modelin boyutu çok büyük olduğu için GitHub’a yüklenememiştir.  
`deneme/m2.py` dosyasını çalıştırdığınızda, eğer belirtilen yolda önceden eğitilmiş bir model yoksa, model eğitilmeye başlanacaktır.

** 📝 Not:** Bu işlem uzun sürebilir ve GPU gerektirebilir.

---

## 📄 Lisans

Bu proje, bitirme projesi olarak **Burak Reis ÇIBIK** ve **Kubilay ATA** tarafından geliştirilmiştir.

---

## ⚠️ Önemli
Projede kullanılan Kaggle üzerinde paylaşılmış olan veri setinin bağlantısını bulamadım ve bu nedenle ekleyemedim. Veri setini oluşturan ve paylaşan kişiye buradan teşekkür ediyoruz. :)
