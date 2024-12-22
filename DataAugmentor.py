from keras.preprocessing.image import ImageDataGenerator
import numpy as np
class DataAugmentor:
    def augment_data(self):
        datagen = ImageDataGenerator(
            rescale=1.0 / 255.0,  # Normalizasyon
            rotation_range=20,  # Görselleri döndür
            width_shift_range=0.2,  # Genişlikte kaydır
            height_shift_range=0.2,  # Yükseklikte kaydır
            shear_range=0.2,  # Kesme işlemi slicing
            zoom_range=0.2,  # Yakınlaştır
            horizontal_flip=True,  # Görselleri yatay çevir
            fill_mode='nearest',  # Boşluk doldur
            brightness_range=[0.8, 1.2],  # Parlaklık artır
            preprocessing_function=self.add_random_noise  # Gürültü artır
        )
        return datagen

    @staticmethod
    def add_random_noise(image):
        noise = np.random.normal(0, 0.05, image.shape)  # Gürültü ekle
        image_with_noise = np.clip(image + noise, 0, 1)
        return image_with_noise
