# Face Authentication System


## Overview

Offline-First Face Authentication System is a privacy-focused biometric authentication solution that performs facial verification without relying on cloud-based services. The system is designed to operate in low-connectivity or offline-first environments, making it suitable for secure identity verification where internet access is limited or unavailable.

The solution combines a React Native mobile application with a Flask backend and MediaPipe-based face detection pipeline. Facial features are extracted locally and matched against a stored database of face encodings to authenticate users.

---

## Why This Project Matters

Most modern face authentication systems depend on cloud APIs, which introduce privacy risks, latency, and dependency on stable internet connectivity. This system eliminates cloud dependency by performing biometric processing locally, ensuring better privacy control and usability in offline or constrained environments.

---

## Key Features

* Biometric authentication workflow Mobile-based face capture using React Native (Expo) 
* Flask REST API for local processing
* MediaPipe-based face detection pipeline 
* Local face encoding storage (no cloud database) 
* Lightweight and modular architecture Privacy-preserving design (no external API dependency)

---

## System Architecture

```text
Mobile Application (React Native)
          |
          v
Flask Backend API
          |
          v
 MediaPipe Face Detection
          |
          v
 Feature Extraction Module
          |
          v
 Face Matching Engine
          |
          v
 Authentication Result
```

---

## Technology Stack

### Frontend  (Mobile App)

* React Native
* Expo
* TypeScript

### Backend

* Python
* Flask
* OpenCV
* MediaPipe
* NumPy

### Storage

*  Pickle-based local face encoding database (.pkl)

---

## Project Structure

```text
offline-face-authentication/
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
├── future_mobile_app/
│   ├── app/
│   ├── assets/
│   ├── components/
│   └── package.json
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Installation

### Backend Setup

```bash
git clone https://github.com/sruthianilkumar/offline-face-authentication.git

cd offline-face-authentication

pip install -r requirements.txt

python backend/api.py
```

Backend will start on:

```text
http://localhost:5000
```

---

### Mobile Application Setup

```bash
cd future_mobile_app

npm install

npx expo start
```

Scan the QR code using Expo Go to run the application on a mobile device.

---

## Usage Flow

1. Start the Flask backend.
2. Launch the mobile application.
3. Grant camera permission.
4. Capture a face image.
5. Image is sent to the backend.
6. API MediaPipe extracts facial features.
7. Features are matched with stored encodings.
8. Authentication result is returned to the app.

---

## Current Limitations

* Prototype-level recognition accuracy 
* Sensitive to lighting and image quality
* Limited dataset for testing 
* Requires further real-device testing for production use

---

## Future Improvements

* FaceNet or ArcFace embeddings
* Liveness detection
* Offline encrypted user database
* Multi-user support
* Improved mobile UI
* Enhanced recognition accuracy

---

## Impact

This project demonstrates a privacy-first approach to biometric authentication that avoids cloud dependency and enables secure identity verification in offline-first environments. It can be extended for use in rural systems, secure access control, and edge computing applications where connectivity is unreliable.

---

## License

This project is intended for educational and hackathon demonstration purposes.

---

