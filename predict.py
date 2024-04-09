# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.preprocessing.text import Tokenizer

# # Load the tokenizer
# tokenizer = Tokenizer(num_words=10000)
# # Assuming tokenizer is trained on the same data as before
# # Load the saved model
# model = load_model("spam_detection_model.h5")

# # Function to preprocess input text
# def preprocess_text(text):
#     # Tokenize the text
#     seq = tokenizer.texts_to_sequences([text])
#     # Pad sequences
#     pad_seq = pad_sequences(seq, maxlen=100)
#     return pad_seq

# # Function to predict whether input text is spam or not
# # Function to predict whether input text is spam or not
# def predict_spam(text, threshold=0.5):
#     preprocessed_text = preprocess_text(text)
#     prediction = model.predict(preprocessed_text)[0][0]
#     if prediction >= threshold:
#         return "Spam"
#     else:
#         return "Not Spam"

# # Example usage with adjusted threshold
# user_input = input("Enter text to check if it's spam or not: ")
# prediction_result = predict_spam(user_input, threshold=0.3)
# print("Prediction:", prediction_result)