# Offline Face Authentication

## Overview

Offline Face Authentication is a privacy-focused authentication system that performs facial verification without relying on cloud services. The project combines a React Native mobile application with a Flask backend and MediaPipe-based face detection.

The system captures a face image from a mobile device, sends it to a backend API, extracts facial features, and compares them against locally stored face encodings to identify the user.

---

## Project Goal

The objective of this project is to provide a lightweight, privacy-preserving face authentication solution that can operate without continuous internet connectivity. The system is designed as a proof-of-concept for secure identity verification in offline or low-connectivity environments.

---

## Features

* Mobile face capture using React Native (Expo)
* Flask REST API backend
* MediaPipe face detection
* Local face encoding storage
* Offline authentication workflow
* Lightweight and privacy-friendly design

---

## Architecture

```text
React Native Mobile App
          |
          v
      Flask API
          |
          v
 MediaPipe Face Detection
          |
          v
 Feature Extraction
          |
          v
 Face Matching Engine
          |
          v
 Authentication Result
```

---

## Technology Stack

### Frontend

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

* Pickle (.pkl) encoded face database

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

## Usage

1. Start the Flask backend.
2. Launch the mobile application.
3. Grant camera permission.
4. Capture a face image.
5. Image is sent to the backend.
6. Face features are extracted and matched.
7. Authentication result is displayed.

---

## Demo Flow

1. User opens the mobile application.
2. Camera captures a face image.
3. Image is transmitted to the Flask backend.
4. MediaPipe detects the face.
5. Facial features are extracted.
6. Features are compared against stored encodings.
7. Authentication result is returned to the application.

---

## Current Limitations

* Basic feature extraction approach
* Mobile camera integration requires additional device-specific testing
* Authentication accuracy depends on image quality
* Limited face dataset for testing
* Prototype implementation intended for demonstration purposes

---

## Future Improvements

* FaceNet or ArcFace embeddings
* Liveness detection
* Offline encrypted user database
* Multi-user support
* Improved mobile UI
* Enhanced recognition accuracy

---

## Hackathon Submission Notes

This project demonstrates an offline-first face authentication workflow designed for privacy-conscious environments. The solution avoids cloud-based face recognition services and performs authentication using locally stored face encodings.

The architecture is modular and can be extended with stronger facial embeddings, liveness detection, and secure storage mechanisms in future versions.

