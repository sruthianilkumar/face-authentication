import cv2
import mediapipe as mp
import numpy as np
import pickle

ENCODINGS_FILE = "models/encodings.pkl"

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

def load_data():
    with open(ENCODINGS_FILE, "rb") as f:
        return pickle.load(f)

def match(face_vec, encodings, labels):
    best_label = "Unknown"
    min_dist = float("inf")

    for enc, label in zip(encodings, labels):
        dist = np.linalg.norm(face_vec - enc)

        if dist < min_dist:
            min_dist = dist
            best_label = label

    if min_dist < 2.0:
        return best_label
    return "Unknown"


if __name__ == "__main__":
    data = load_data()

    test_img = "data/s/0.jpg"   # change if needed
    image = cv2.imread(test_img)

    features = extract_features(image)

    if features is None:
        print("No face detected")
    else:
        result = match(features, data["encodings"], data["labels"])
        print("Result:", result)
