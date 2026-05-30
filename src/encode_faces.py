import os
import cv2
#import face_recognition
import numpy as np
import pickle

DATASET_PATH = "../data"
ENCODINGS_FILE = "../models/encodings.pkl"


def encode_faces():
    known_encodings = []
    known_names = []

    # Loop through each user folder
    for user_name in os.listdir(DATASET_PATH):
        user_folder = os.path.join(DATASET_PATH, user_name)

        if not os.path.isdir(user_folder):
            continue

        print(f"Processing user: {user_name}")

        for img_name in os.listdir(user_folder):
            img_path = os.path.join(user_folder, img_name)

            image = cv2.imread(img_path)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # detect face locations
            boxes = face_recognition.face_locations(rgb)

            # compute encodings
            encodings = face_recognition.face_encodings(rgb, boxes)

            for enc in encodings:
                known_encodings.append(enc)
                known_names.append(user_name)

    # Save encodings
    data = {
        "encodings": known_encodings,
        "names": known_names
    }

    os.makedirs("../models", exist_ok=True)

    with open(ENCODINGS_FILE, "wb") as f:
        pickle.dump(data, f)

    print("Encodings saved successfully!")


if __name__ == "__main__":
    encode_faces()
