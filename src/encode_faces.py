import os
import cv2
import mediapipe as mp
import numpy as np
import pickle

DATASET_PATH = "data"
OUTPUT_FILE = "models/encodings.pkl"

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

def extract_features(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return None

    landmarks = results.multi_face_landmarks[0].landmark

    vector = []
    for lm in landmarks:
        vector.append(lm.x)
        vector.append(lm.y)

    return np.array(vector)

def encode_faces():
    encodings = []
    labels = []

    for user in os.listdir(DATASET_PATH):
        user_path = os.path.join(DATASET_PATH, user)

        if not os.path.isdir(user_path):
            continue

        print("Processing:", user)

        for img_name in os.listdir(user_path):
            img_path = os.path.join(user_path, img_name)

            image = cv2.imread(img_path)
            features = extract_features(image)

            if features is not None:
                encodings.append(features)
                labels.append(user)

    os.makedirs("models", exist_ok=True)

    with open(OUTPUT_FILE, "wb") as f:
        pickle.dump({
            "encodings": encodings,
            "labels": labels
        }, f)

    print("Encodings saved successfully!")

if __name__ == "__main__":
    encode_faces()
