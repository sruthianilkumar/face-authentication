import cv2
import mediapipe as mp


class FaceService:
    """
    Handles face detection and face capture using webcam.
    Reusable service for registration and verification.
    """

    def __init__(self):
        self.mp_face = mp.solutions.face_detection
        self.face_detector = self.mp_face.FaceDetection(
            model_selection=0,
            min_detection_confidence=0.5
        )

    def detect_faces(self, frame):
        """
        Detect faces in a frame and return bounding boxes.
        """
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_detector.process(rgb)

        faces = []
        h, w, _ = frame.shape

        if results.detections:
            for det in results.detections:
                bbox = det.location_data.relative_bounding_box

                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                w_box = int(bbox.width * w)
                h_box = int(bbox.height * h)

                faces.append((x, y, w_box, h_box))

        return faces

    def capture_face_from_webcam(self):
        """
        Opens webcam, detects face, and captures a processed face image.
        Press SPACE to capture, Q to quit.
        """
        cap = cv2.VideoCapture(0)

        print("Press SPACE to capture face, Q to quit")

        while True:
            ret, frame = cap.read()
            if not ret:
                continue

            faces = self.detect_faces(frame)

            # Draw bounding boxes
            for (x, y, w_box, h_box) in faces:
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

            # Quit
            if key == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return None

            # Capture
            if key == 32:
                if len(faces) == 0:
                    print("No face detected - try again")
                    continue

                x, y, w_box, h_box = faces[0]

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face = gray[y:y + h_box, x:x + w_box]

                # Normalize size
                face = cv2.resize(face, (100, 100))

                cap.release()
                cv2.destroyAllWindows()

                return face
