from proje.CNNModel import CNNModel
from proje.DataAugmentor import DataAugmentor
from proje.DatasetManager import DatasetManager
from proje.DatasetSplitter import DatasetSplitter
from proje.ImagePreprocessor import ImagePreprocessor

def main():
    try:
        # Data filter ve copy işlemleri
        dataset_manager = DatasetManager(
            source_folder="C:\\Users\\...\\Downloads\\JPEGImages",
            target_folder="FilteredImages",
            selected_classes=["collie", "dolphin", "elephant", "fox", "moose", "rabbit", "sheep", "squirrel", "seal", "cow"],
            max_images_per_class=650
        )
        dataset_manager.filter_and_copy()

        # Görselleri ön işleme sok.
        preprocessor = ImagePreprocessor(image_size=(128, 128))
        X, y = preprocessor.preprocess_images("FilteredImages")
        if X is None or y is None:
            print("Preprocessing failed. Exiting...")
            return

        # Veriyi split et
        splitter = DatasetSplitter()
        X_train, X_test, y_train, y_test = splitter.split_data(X, y)

        #Data Augmentation -> Veri Artırma
        augmentor = DataAugmentor()
        datagen = augmentor.augment_data()
        datagen.fit(X_train)

        # Modelin egitilmesi
        cnn_model = CNNModel(input_shape=(128, 128, 3), num_classes=10)
        cnn_model.train(X_train, y_train, X_test, y_test, epochs=20)
        cnn_model.evaluate(X_test, y_test)

    except Exception as e:
        print(f"Error in main process: {e}")

if __name__ == "__main__":
    main()
