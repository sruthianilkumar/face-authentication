from flask import Flask, request, jsonify
import cv2
import numpy as np
import pickle
import mediapipe as mp

app = Flask(__name__)

# =========================
# LOAD ENCODINGS
# =========================
ENCODINGS_FILE = "models/encodings.pkl"

with open(ENCODINGS_FILE, "rb") as f:
    data = pickle.load(f)

# =========================
# MEDIAPIPE FACE DETECTION
# =========================
mp_face = mp.solutions.face_detection
face_detector = mp_face.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.3
)

# =========================
# FEATURE EXTRACTION
# =========================
def extract_features(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detector.process(rgb)

    if not results.detections:
        return None

    h, w, _ = image.shape

    # take first detected face
    det = results.detections[0]
    bbox = det.location_data.relative_bounding_box

    x = int(bbox.xmin * w)
    y = int(bbox.ymin * h)
    w_box = int(bbox.width * w)
    h_box = int(bbox.height * h)

    # safety check
    x, y = max(0, x), max(0, y)

    face = image[y:y + h_box, x:x + w_box]

    if face.size == 0:
        return None

    face = cv2.resize(face, (100, 100))
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    # flatten to vector
    return gray.flatten()

# =========================
# MATCH FUNCTION
# =========================
def match(face_vec):
    best_label = "Unknown"
    min_dist = float("inf")

    for enc, label in zip(data["encodings"], data["labels"]):
        dist = np.linalg.norm(face_vec - enc)

        if dist < min_dist:
            min_dist = dist
            best_label = label

    # threshold (tune if needed)
    if min_dist < 2500:
        return best_label, float(min_dist)

    return "Unknown", float(min_dist)

# =========================
# API ROUTE
# =========================
@app.route("/")
def home():
    return "Face Auth API is running"
    
@app.route("/auth", methods=["POST"])
def auth():
    try:
        if "image" not in request.files:
            return jsonify({
               "status": "fail",
               "msg": "No image uploaded"
             }), 400
        file = request.files["image"]

        img_bytes = np.frombuffer(file.read(), np.uint8)
        frame = cv2.imdecode(img_bytes, cv2.IMREAD_COLOR)
        if frame is None:
           return jsonify({
            "status": "fail",
            "msg": "Invalid image"
           }), 400
        features = extract_features(frame)

        if features is None:
            return jsonify({
                "status": "fail",
                "msg": "No face detected"
            })

        label, dist = match(features)

        return jsonify({
            "status": "success",
            "user": label,
            "distance": dist
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "msg": str(e)
        })

# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
