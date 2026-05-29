import cv2
import os

def capture_faces(user_name):
    cam = cv2.VideoCapture(0)

    save_path = f"data/{user_name}"
    os.makedirs(save_path, exist_ok=True)

    count = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        cv2.imshow("Face Capture (Press S to save, Q to quit)", frame)

        key = cv2.waitKey(1)

        if key == ord('s'):
            img_path = f"{save_path}/{count}.jpg"
            cv2.imwrite(img_path, frame)
            count += 1
            print("Saved:", img_path)

        elif key == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    name = input("Enter user name: ")
    capture_faces(name)
