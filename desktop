import cv2

for i in range(5):
    cap = cv2.VideoCapture(i)

    if cap.isOpened():
        ret, frame = cap.read()

        print(f"Camera {i}: opened={cap.isOpened()} ret={ret}")

        if ret:
            print("Frame shape:", frame.shape)

        cap.release()
    else:
        print(f"Camera {i}: not available")
