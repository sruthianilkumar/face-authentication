import os
import sys

def menu():
    print("\n==============================")
    print(" OFFLINE FACE AUTH SYSTEM ")
    print("==============================")
    print("1. Capture Faces")
    print("2. Encode Faces")
    print("3. Authenticate")
    print("4. Exit")
    print("==============================")

def run_capture():
    print("\n📸 Starting Face Capture...\n")
    os.system("python src/capture_faces.py")

def run_encode():
    print("\n🧠 Encoding Faces...\n")
    os.system("python src/encode_faces.py")

def run_auth():
    print("\n🔍 Starting Authentication...\n")
    os.system("python src/authenticate.py")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            run_capture()

        elif choice == "2":
            run_encode()

        elif choice == "3":
            run_auth()

        elif choice == "4":
            print("Exiting system... 👋")
            sys.exit()

        else:
            print("❌ Invalid choice! Try again.")
