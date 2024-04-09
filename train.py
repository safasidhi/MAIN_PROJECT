import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Flatten, Dense
from tensorflow.keras.models import load_model

# Load dataset
data = pd.read_csv("spam_ham_dataset.csv")

# Preprocessing
X = data['text']
y = data['label_num']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tokenization
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(X_train)
X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)
X_train_pad = pad_sequences(X_train_seq, maxlen=100)
X_test_pad = pad_sequences(X_test_seq, maxlen=100)

# Model definition
model = Sequential()
model.add(Embedding(10000, 16))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Training
model.fit(X_train_pad, y_train, epochs=10, batch_size=32, validation_data=(X_test_pad, y_test))

# Evaluation
loss, accuracy = model.evaluate(X_test_pad, y_test)
print("Test Accuracy:", accuracy)

# Save the model
model.save("spam_detection_model.h5")

# Function to preprocess input text
def preprocess_text(text):
    # Tokenize the text
    seq = tokenizer.texts_to_sequences([text])
    # Pad sequences
    pad_seq = pad_sequences(seq, maxlen=100)
    return pad_seq

# Function to predict whether input text is spam or not
def predict_spam(text):
    preprocessed_text = preprocess_text(text)
    prediction = model.predict(preprocessed_text)[0][0]
    if prediction >= 0.5:
        return "Spam"
    else:
        return "Not Spam"

# Example usage
# user_input = input("Enter text to check if it's spam or not: ")
# prediction_result = predict_spam(user_input)
# print("Prediction:", prediction_result)