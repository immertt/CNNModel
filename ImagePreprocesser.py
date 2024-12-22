import cv2
import numpy as np
import os
from keras.utils import to_categorical

class ImagePreprocessor:
    def __init__(self, image_size=(128, 128)):
        self.image_size = image_size

    def preprocess_images(self, dataset_path):
        images = []
        labels = []

        try:
            for class_name in os.listdir(dataset_path):
                class_path = os.path.join(dataset_path, class_name)
                if os.path.isdir(class_path):
                    for image_name in os.listdir(class_path):
                        image_path = os.path.join(class_path, image_name)
                        image = cv2.imread(image_path)
                        if image is None:
                            print(f"Warning: Could not read image {image_path}. Skipping...")
                            continue
                        img_resized = cv2.resize(image, self.image_size)
                        img_normalized = img_resized / 255.0
                        images.append(img_normalized)
                        labels.append(class_name)

            if not images or not labels:
                raise ValueError("No valid images found in the dataset path.")

            images = np.array(images)
            class_names = sorted(os.listdir(dataset_path))
            class_to_index = {class_name: index for index, class_name in enumerate(class_names)}
            labels = np.array([class_to_index[label] for label in labels])
            labels = to_categorical(labels, num_classes=len(class_names)).astype(np.float32)

            return images, labels

        except Exception as e:
            print(f"Error during image preprocessing: {e}")
            return None, None
