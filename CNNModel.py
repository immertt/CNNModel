from keras import regularizers
from keras.callbacks import EarlyStopping
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout
from keras.optimizers import Adam
from keras.layers import Dense
import matplotlib.pyplot as plt
class CNNModel:
    def __init__(self, input_shape, num_classes):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = self.build_model()

    def build_model(self):
        model = Sequential([
            Conv2D(32, (3, 3), activation='relu',
                   kernel_regularizer=regularizers.l2(0.01), input_shape=self.input_shape),
            MaxPooling2D((2, 2)),
            Dropout(0.4),  # Dropout artırıldı
            Conv2D(64, (3, 3), activation='relu',
                   kernel_regularizer=regularizers.l2(0.01)),
            MaxPooling2D((2, 2)),
            Dropout(0.4),
            Flatten(),
            Dense(128, activation='relu',kernel_regularizer=regularizers.l2(0.01)),
            Dropout(0.5),
            Dense(self.num_classes, activation='softmax')
        ])
        model.compile(optimizer=Adam(learning_rate=0.001),
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
        return model

    def train(self, X_train, y_train, X_test, y_test, epochs=10, batch_size=32):
        # Early Stopping callback
        early_stopping = EarlyStopping(
            monitor='val_loss', patience=5, restore_best_weights=True)

        history = self.model.fit(
            X_train, y_train,
            validation_data=(X_test, y_test),
            epochs=epochs,
            batch_size=batch_size,
            callbacks=[early_stopping]
        )

        # Training, loss validation
        plt.figure(figsize=(12, 6))
        plt.plot(history.history['loss'], label='Training Loss')
        plt.plot(history.history['val_loss'], label='Validation Loss')
        plt.title('Model Loss Over Epochs')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.show(block=True)

        # Trainnging, accuracy validation
        plt.figure(figsize=(12, 6))
        plt.plot(history.history['accuracy'], label='Training Accuracy')
        plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
        plt.title('Model Accuracy Over Epochs')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.show(block=True)

        return history

    def evaluate(self, X_test, y_test):
        loss, accuracy = self.model.evaluate(X_test, y_test)
        print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}")
        return loss, accuracy
