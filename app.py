import sys
from src import capture_faces, encode_faces, authenticate

def menu():
    print("\n==============================")
    print(" OFFLINE FACE AUTH SYSTEM ")
    print("==============================")
    print("1. Capture Faces")
    print("2. Encode Faces")
    print("3. Authenticate (LIVE)")
    print("4. Exit")
    print("==============================")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            capture_faces.capture_faces(name)

        elif choice == "2":
            encode_faces.encode_faces()

        elif choice == "3":
            authenticate.run()

        elif choice == "4":
            sys.exit()

        else:
            print("Invalid choice")
