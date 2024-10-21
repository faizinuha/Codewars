from tensorflow.keras.models import load_model
import numpy as np

# Load pre-trained age detection model
age_model = load_model('age_model.h5')

# Function to predict age
def predict_age(face):
    face = cv2.resize(face, (64, 64))  # Resize to the model's expected input size
    face = face / 255.0  # Normalize the image
    face = np.expand_dims(face, axis=0)  # Expand dimensions to match the input shape of the model
    age = age_model.predict(face)
    return int(age[0][0])

# Integrate with the previous code
# Replace cv2.rectangle line with:
for (x, y, w, h) in faces:
    face = frame[y:y+h, x:x+w]
    age = predict_age(face)
    cv2.putText(frame, f'Age: {age}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
