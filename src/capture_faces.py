import cv2
import os

def capture_faces(user_name):
    cam = cv2.VideoCapture(0, cv2.CAP_V4L2)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    save_path = f"data/{user_name}"
    os.makedirs(save_path, exist_ok=True)

    count = len(os.listdir(save_path))

    while True:
        ret, frame = cam.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # show rectangles (debug)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Camera (S=save, Q=quit)", frame)

        key = cv2.waitKey(1) & 0xFF

        # ✅ FIX: allow saving ALWAYS (not dependent on detection)
        if key == ord('s'):
            if len(faces) > 0:
                x, y, w, h = faces[0]
                face = frame[y:y+h, x:x+w]
                print("Face detected → saving cropped face")
            else:
                face = frame
                print("No face detected → saving full frame")

            img_path = f"{save_path}/{count}.jpg"
            cv2.imwrite(img_path, face)
            count += 1
            print("Saved:", img_path)

        elif key == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    name = input("Enter user name: ")
    capture_faces(name)
