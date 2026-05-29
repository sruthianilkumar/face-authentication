import cv2
import mediapipe as mp
print(mp.solutions)
from flask import Flask, jsonify



class FaceService:
    def __init__(self):
        mp_face = mp.solutions.face_detection
        self.face_detector = mp_face.FaceDetection(
            model_selection=0,
            min_detection_confidence=0.5
        )

    def capture_face(self):
        cap = cv2.VideoCapture(0)

        print("Press SPACE to capture face, Q to quit")

        while True:
            ret, frame = cap.read()

            if not ret:
                continue

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.face_detector.process(rgb)

            faces = []

            if results.detections:
                for det in results.detections:
                    bbox = det.location_data.relative_bounding_box
                    h, w, _ = frame.shape

                    x = int(bbox.xmin * w)
                    y = int(bbox.ymin * h)
                    w_box = int(bbox.width * w)
                    h_box = int(bbox.height * h)

                    faces.append((x, y, w_box, h_box))

                    cv2.rectangle(
                        frame,
                        (x, y),
                        (x + w_box, y + h_box),
                        (0, 255, 0),
                        2
                    )

            cv2.putText(
                frame,
                "Align face & press SPACE",
                (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 0),
                2
            )

            cv2.imshow("Face Capture", frame)

            key = cv2.waitKey(1)

            if key == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return None

            if key == 32:
                if len(faces) == 0:
                    print("No face detected - try again")
                    continue

                x, y, w, h = faces[0]

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face = gray[y:y + h, x:x + w]

                face = cv2.resize(face, (100, 100))

                cap.release()
                cv2.destroyAllWindows()

                return face
                
                
app = Flask(__name__)

face_service = FaceService()   # ✅ create object


@app.route("/capture")
def capture():
    face = face_service.capture_face()   # ✅ correct call

    if face is None:
        return jsonify({"status": "failed"})

    return jsonify({
        "status": "success",
        "shape": str(face.shape)
    })
    
    
