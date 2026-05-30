import cv2
#import face_recognition
import pickle
import numpy as np

ENCODINGS_FILE = "../models/encodings.pkl"


def load_encodings():
    with open(ENCODINGS_FILE, "rb") as f:
        data = pickle.load(f)
    return data


def authenticate():
    data = load_encodings()

    video = cv2.VideoCapture(0)

    print("Starting authentication... Press Q to quit")

    while True:
        ret, frame = video.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        names = []

        for enc in encodings:
            matches = face_recognition.compare_faces(
                data["encodings"], enc
            )

            name = "Unknown"

            face_distances = face_recognition.face_distance(
                data["encodings"], enc
            )

            best_match = np.argmin(face_distances)

            if matches[best_match]:
                name = data["names"][best_match]

            names.append(name)

        # Display results
        for (top, right, bottom, left), name in zip(boxes, names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Authentication", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    authenticate()
