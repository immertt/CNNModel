#Veri setini okur, sınıfları filtreler, resimleri işler.
import os
import shutil

class DatasetManager:
    def __init__(self, source_folder, target_folder, selected_classes, max_images_per_class=650):
        self.source_folder = source_folder # hangi klasörden veri alacagız
        self.target_folder = target_folder #hangi klasöre veriyi kopyalayacagız
        self.selected_classes = selected_classes #hangi sınıfları seçecegiz
        self.max_images_per_class = max_images_per_class #kaç tane resim alacagız.

    def filter_and_copy(self):
        try:
            if not os.path.exists(self.source_folder):
                raise FileNotFoundError(f"Source folder '{self.source_folder}' not found.")

            if not os.path.exists(self.target_folder):
                os.makedirs(self.target_folder)

            for class_name in self.selected_classes:
                source_class_path = os.path.join(self.source_folder, class_name)
                target_class_path = os.path.join(self.target_folder, class_name)

                if not os.path.exists(source_class_path):
                    print(f"Warning: Class '{class_name}' not found in source folder. Skipping...")
                    continue

                os.makedirs(target_class_path, exist_ok=True)
                image_files = os.listdir(source_class_path)[:self.max_images_per_class]

                for image_file in image_files:
                    shutil.copy(os.path.join(source_class_path, image_file), target_class_path)

        except Exception as e:
            print(f"Error during dataset filtering and copying: {e}")
