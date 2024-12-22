
# CNN Image Classification Project  

## 📚 **Proje Açıklaması**  
Bu proje, Convolutional Neural Network (CNN) kullanarak görüntü sınıflandırma işlemini gerçekleştirmeyi amaçlamaktadır. Projede veri artırma (data augmentation), düzenleme (regularization), erken durdurma (early stopping) ve model performansını iyileştiren diğer teknikler uygulanmıştır. Model, parlaklık, kontrast ve gürültü manipülasyonları içeren veri setleri üzerinde eğitilmiş ve test edilmiştir.  

## 🚀 **Özellikler**  
- **Veri Çoğaltma (Data Augmentation):** Görsellerde döndürme, yakınlaştırma, parlaklık ve gürültü gibi çeşitli manipülasyonlar uygulanarak veri çeşitliliği artırılmıştır.  
- **Regularization:** Aşırı öğrenmeyi önlemek için Dropout ve L2 düzenlemesi kullanılmıştır.  
- **Erken Durdurma (Early Stopping):** Modelin doğrulama kaybında iyileşme görülmediğinde eğitim süreci durdurulur.  
- **Model Performans Görselleştirmesi:** Eğitim ve doğrulama kayıpları ile doğruluk oranları grafiklerle gösterilmektedir.  

## 📂 **Proje Yapısı**  
```
.
├── data                # Veri setleri
├── models              # Eğitilmiş modellerin kaydedildiği klasör
├── src                 # Kaynak kodlar
│   ├── augmentor.py    # Veri çoğaltma sınıfı
│   ├── cnn_model.py    # CNN model sınıfı
│   ├── train.py        # Eğitim kodları
├── requirements.txt    # Gerekli Python kütüphaneleri
├── README.md           # Proje açıklama dosyası
```

## ⚙️ **Kullanılan Teknolojiler ve Kütüphaneler**  
- **TensorFlow / Keras**: CNN modeli ve veri artırma için.  
- **NumPy**: Matematiksel işlemler.  
- **Matplotlib**: Eğitim sürecinin görselleştirilmesi.  
- **Python 3.8+**  

## 🛠️ **Nasıl Çalıştırılır?**  

1. **Proje Dosyalarını Klonlayın:**  
   ```bash
   git clone https://github.com/kullaniciadi/proje-adi.git
   cd proje-adi
   ```

2. **Gerekli Kütüphaneleri Yükleyin:**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Modeli Eğitin:**  
   ```bash
   python src/train.py
   ```

4. **Sonuçları Görselleştirin:**  
   Eğitim tamamlandıktan sonra `Matplotlib` ile kayıp ve doğruluk grafikleri görüntülenir.  

## 📊 **Sonuçlar ve Performans**  
Model, doğrulama setinde %XX doğruluk oranına ulaşmıştır. Eğitim süreci boyunca `EarlyStopping` ve `Dropout` gibi teknikler sayesinde aşırı öğrenme önlenmiştir.  

## 📈 **Geliştirme Planları**  
- Daha büyük ve çeşitli veri setleriyle test edilmesi.  
- Transfer learning teknikleri eklenmesi.  
- Kullanıcı arayüzü ile modelin entegrasyonu.  

## 🤝 **Katkı Sağlayın**  
Herhangi bir hata bulursanız veya yeni özellikler eklemek isterseniz lütfen bir **pull request** gönderin veya **issue** açın.  

## 📄 **Lisans**  
Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.  
