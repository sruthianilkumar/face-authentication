# Face Authentication System  

---

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![React Native](https://img.shields.io/badge/React%20Native-Mobile-61DAFB?logo=react)
![Expo](https://img.shields.io/badge/Expo-React%20Native-000020?logo=expo)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-AI-orange)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy)

![Offline](https://img.shields.io/badge/Mode-Offline--First-success)
![Privacy](https://img.shields.io/badge/Privacy-No%20Cloud-important)
![Status](https://img.shields.io/badge/Status-Hackathon%20Project-purple)

</p>

<p align="center">
  <img src="assets/banner1.png" alt="Face Authentication System Banner" />
</p>

---

## 🚀 One-Line Pitch

A **fully offline face authentication system** that performs secure biometric verification on-device using **React Native, Flask, and MediaPipe**, without sending any data to the cloud.

---

## 🎯 Problem Statement

Most face authentication systems today depend on cloud services, which cause:

- ❌ Privacy risks (biometric data exposed externally)
- ❌ Internet dependency
- ❌ High latency
- ❌ Unusable in low-connectivity regions

---

## 💡 Solution

I built a **fully offline-first biometric authentication system** that:

✔ Works without internet  
✔ Keeps all biometric data local  
✔ Processes face recognition on-device/server locally  
✔ Ensures privacy by design  

---

## ⚡ Key Highlights

- 📱 Mobile face capture using **React Native (Expo)**
- 🧠 Face detection using **MediaPipe**
- ⚙️ Backend processing with **Flask API**
- 💾 Local face encoding database (.pkl)
- 🔐 Fully offline authentication pipeline
- 🧩 Lightweight & modular architecture

---

## 🏗 System Architecture

```
Mobile App (React Native)
        ↓
Flask Backend API
        ↓
MediaPipe Face Detection
        ↓
Feature Extraction
        ↓
Face Matching Engine
        ↓
Authentication Result
```

---

## 🛠 Tech Stack

**Frontend**
- React Native
- Expo
- TypeScript

**Backend**
- Python
- Flask
- OpenCV
- MediaPipe
- NumPy

**Storage**
- Local Pickle-based Face Encodings (.pkl)

---

## 📂 Project Structure

```
face-authentication/
│
├── backend/              # Flask API
├── data/                 # Face images dataset
├── models/               # Encoded face embeddings
├── src/                  # Face processing scripts
├── mobile_app/           # React Native app
├── requirements.txt      # Python dependencies
└── LICENSE
```

---

## ⚙️ How It Works

1. User opens mobile app  
2. Captures face using camera  
3. Image sent to Flask backend  
4. MediaPipe detects face landmarks  
5. Features extracted and encoded  
6. Compared with stored embeddings  
7. Authentication result returned  

---

## ▶️ Setup Instructions

### 🔧 Backend

```bash
git clone https://github.com/sruthianilkumar/face-authentication.git
cd face-authentication
pip install -r requirements.txt
python backend/api.py
```

Backend runs at:

```
http://localhost:5000
```

---

### 📱 Mobile App

```bash
cd mobile_app
npm install
npx expo start
```

Scan QR using **Expo Go**.

---

## ⚠️ Limitations

- Prototype-level accuracy  
- Sensitive to lighting conditions  
- Small dataset used for testing  
- Requires real-device testing  

---

## 🚀 Future Scope

- FaceNet / ArcFace integration  
- Liveness detection (anti-spoofing)  
- Encrypted biometric storage  
- Multi-user authentication system  
- Improved mobile UI/UX  
- Edge-device optimization  

---

## 📊 Real-World Impact

This project demonstrates a **privacy-first biometric authentication model** suitable for:

- 🏥 Rural identity systems  
- 🏫 Campus authentication  
- 🏢 Secure offline access control  
- 🌐 Low-connectivity environments  
- 🧠 Edge AI deployment  

---

## 🏁 License

This project is developed for **educational and hackathon demonstration purposes only**.

---

## 🔥 Why This Project Stands Out

✔ Offline-first architecture  
✔ No cloud dependency  
✔ Privacy-preserving design  
✔ Real-world deployment potential  
✔ Lightweight and scalable  
