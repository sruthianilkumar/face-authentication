#**********************************************************************************************#
########################  FACE AUTHENTICATION FILE   ###########################################
#**********************************************************************************************#
##############################  SRUTHI A K  ####################################################
#**********************************************************************************************#


import cv2
import mediapipe as mp
import numpy as np
import pickle

ENCODINGS_FILE = "models/encodings.pkl"

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def extract_features(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return None

    lm = results.multi_face_landmarks[0].landmark

    vector = []
    for i in range(0, len(lm), 2):  # reduce noise + speed up
        vector.append(lm[i].x)
        vector.append(lm[i].y)

    return np.array(vector)

def load_data():
    with open(ENCODINGS_FILE, "rb") as f:
        return pickle.load(f)

def match(face_vec, encodings, labels):
    best = "Unknown"
    min_dist = 999

    for enc, label in zip(encodings, labels):
        dist = np.linalg.norm(face_vec - enc)

        if dist < min_dist:
            min_dist = dist
            best = label

    if min_dist < 2.2:
        return best, min_dist
    return "Unknown", min_dist


def run():
    data = load_data()

    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

    print("LIVE FACE AUTH STARTED - Press Q to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        features = extract_features(frame)

        label = "No Face"
        dist = ""

        if features is not None:
            label, dist_val = match(features, data["encodings"], data["labels"])
            dist = f"{dist_val:.2f}"

        cv2.putText(frame, f"USER: {label}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        if dist:
            cv2.putText(frame, f"DIST: {dist}", (30, 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0), 2)

        cv2.imshow("Face Authentication", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
