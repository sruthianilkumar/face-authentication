# 🧠 Face Authentication System

## 🚀 Overview

Offline-First Face Authentication System is a privacy-focused biometric authentication solution that performs facial verification without relying on cloud-based services.

The system is designed for **offline-first and low-connectivity environments**, enabling secure identity verification where internet access is limited or unavailable.

It combines a React Native mobile application with a Flask backend and a MediaPipe-based face detection pipeline. Facial features are extracted locally and matched against a stored database of face encodings to authenticate users.

---

## 💡 Why This Project Matters

Modern face authentication systems rely heavily on cloud APIs, leading to:

- Privacy risks (biometric data sent externally)
- Internet dependency
- Latency issues
- Infrastructure limitations

This system eliminates cloud dependency by processing biometric data locally, ensuring:

✔ **Stronger privacy control**  
✔ **Offline usability**  
✔ **Lower latency**  
✔ **Lightweight deployment**

---

## ✨ Key Features

- 📱 Mobile-based face capture using React Native (Expo)  
- ⚡ Flask REST API for local processing  
- 🧠 MediaPipe-based face detection pipeline  
- 💾 Local face encoding storage (no cloud database)  
- 🔄 Offline-first authentication workflow  
- 🧩 Lightweight and modular architecture  
- 🔐 Privacy-preserving design (no external API dependency)

---

## 🏗 System Architecture

```text
Mobile Application (React Native)
          │
          ▼
Flask Backend API
          │
          ▼
MediaPipe Face Detection
          │
          ▼
Feature Extraction Module
          │
          ▼
Face Matching Engine
          │
          ▼
Authentication Result


🛠 Technology Stack

📱 Frontend (Mobile App)
React Native
Expo
TypeScript

🧠 Backend
Python
Flask
OpenCV
MediaPipe
NumPy

💾 Storage
Pickle-based local face encoding database (.pkl)

📂 Project Structure
face-authentication/
│
├── backend/
│   └── api.py
│
├── data/
│   └── face_images/
│
├── models/
│   └── encodings.pkl
│
├── src/
│   ├── capture_faces.py
│   ├── encode_faces.py
│   └── authenticate.py
│
├── mobile_app/
│   ├── app/
│   ├── assets/
│   ├── components/
│   └── package.json
│
├── requirements.txt
└── LICENSE
⚙️ Installation
Backend Setup
git clone https://github.com/sruthianilkumar/face-authentication.git
cd face-authentication
pip install -r requirements.txt
python backend/api.py

Backend runs at:

http://localhost:5000
Mobile App Setup
cd mobile_app
npm install
npx expo start

Scan QR using Expo Go to run on a mobile device.

🔄 Usage Flow
Start Flask backend
Launch mobile application
Grant camera permissions
Capture face image
Send image to backend API
MediaPipe extracts facial features
Features matched with stored encodings
Authentication result returned
⚠️ Limitations
Prototype-level accuracy (depends on dataset size)
Sensitive to lighting and camera quality
Limited dataset for testing
Requires real-device testing for production readiness
🚀 Future Improvements
FaceNet / ArcFace embeddings for higher accuracy
Liveness detection (anti-spoofing)
Encrypted local biometric storage
Multi-user authentication system
Improved mobile UI/UX
Edge-device optimization
📊 Impact

This project demonstrates a privacy-first biometric authentication system that avoids cloud dependency and enables secure identity verification in offline-first environments.

It is suitable for:

Rural authentication systems
Secure offline access control
Edge computing environments
Low-connectivity deployments
🏁 License

This project is intended for educational and hackathon demonstration purposes.
