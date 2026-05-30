import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=True,
    max_num_faces=1,
    refine_landmarks=False
)

image = cv2.imread("data/s/0.jpg")

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

results = face_mesh.process(rgb)

if results.multi_face_landmarks:
    print("Face detected")
    print("Landmarks:", len(results.multi_face_landmarks[0].landmark))
else:
    print("No face detected")
