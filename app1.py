###########    offline-face-authentication  Main file ##################
#----------------------------------------------------------------------#

import cv2
import os
import numpy as np
## to ignore the wayland 
import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

DATA_PATH = "data/users"

# FACE CAPTURE

def capture_face():
    face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml"
)

    cap = cv2.VideoCapture(0)

    print("Press SPACE to capture face, Q to quit")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Camera not accessible")
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.03,
    minNeighbors=3,
    minSize=(80, 80)
)

        # UI text 
        cv2.putText(frame, f"Faces detected: {len(faces)}",
            (50, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Face Capture", frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            return None

        if key == 32:  # SPACE
            if len(faces) == 0:
                print("No face detected - try again")
                continue

            (x, y, w, h) = faces[0]
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (100, 100))

            cap.release()
            cv2.destroyAllWindows()
            return face


# SAVE USER
def enroll_user(name):
    face = capture_face()

    if face is None:
        print("Enrollment cancelled")
        return

    os.makedirs(DATA_PATH, exist_ok=True)

    file_path = os.path.join(DATA_PATH, f"{name}.npy")

    np.save(file_path, face)

    print(f"User {name} enrolled successfully!")

# COMPARE FACES
def compare_faces(face1, face2):
    return np.linalg.norm(face1 - face2)


# AUTHENTICATE USER
def authenticate():
    face = capture_face()

    if face is None:
        return

    if not os.path.exists(DATA_PATH):
        print("No users enrolled")
        return

    min_dist = float("inf")
    identity = "Unknown"

    for file in os.listdir(DATA_PATH):
        stored_face = np.load(os.path.join(DATA_PATH, file))

        dist = compare_faces(face, stored_face)

        if dist < min_dist:
            min_dist = dist
            identity = file.replace(".npy", "")

    if min_dist < 3000:  # threshold (tunable)
        print(f"Access Granted: {identity}")
    else:
        print("Access Denied")


# MAIN MENU
def main():
    while True:
        print("\nOFFLINE FACE AUTH ")
        print("1. Enroll User")
        print("2. Authenticate User")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            enroll_user(name)

        elif choice == "2":
            authenticate()

        elif choice == "3":
            print(" Exiting....")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
