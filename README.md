# SAFE_DISTANCE_M

> An AI-powered human detection and safe distance monitoring system built for the NVIDIA Jetson Orin Nano using YOLO11, Computer Vision, and Edge AI.

---

## 📌 About the Project

The project is being developed for deployment on the **NVIDIA Jetson Orin Nano** using the **Skydroid C12 Thermal + 2K HD Dynamic Tracking Camera**.

Rather than creating just another object detection project, the goal is to build a complete edge AI application that combines computer vision, tracking, intelligent decision making, and autonomous monitoring into a single system.

---

## 🎯 Project Objectives

- Detect humans in real time using YOLO11
- Track multiple people simultaneously
- Estimate safe distances between people
- Generate alerts for unsafe distancing
- Integrate with a 3-axis gimbal for automatic target tracking
- Support RGB and Thermal camera inputs
- Deploy the complete application on NVIDIA Jetson Orin Nano
- Run efficiently using TensorRT optimization

---

## 🛠 Tech Stack

### Programming Language

- Python

### AI & Computer Vision

- YOLO11
- OpenCV
- PyTorch
- ByteTrack

### Edge AI

- NVIDIA Jetson Orin Nano
- CUDA
- TensorRT

### Development

- Docker
- Git
- GitHub
- VS Code
- Ubuntu (WSL2)

---

## 📂 Project Structure

```text
SAFE_DISTANCE_M/

├── src/
├── models/
├── config/
├── logs/
├── output/
├── tests/
├── docs/
├── docker/
├── scripts/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🚀 Current Progress

- [x] Project planning
- [x] Development environment setup
- [x] GitHub repository
- [x] Docker environment
- [x] YOLO11 integration
- [x] Human detection architecture
- [x] Software module design
- [ ] Jetson Orin Nano deployment
- [ ] Skydroid camera integration
- [ ] TensorRT optimization
- [ ] Gimbal control
- [ ] Final testing

---

## 📖 Development Roadmap

The project is being developed in multiple phases.

### Phase 1

Development Environment

- Git
- VS Code
- WSL2
- Ubuntu
- Docker

### Phase 2

AI Environment

- Python
- OpenCV
- YOLO11
- PyTorch

### Phase 3

Human Detection

- Person detection
- Bounding boxes
- Confidence estimation

### Phase 4

Tracking Pipeline

- Human tracking
- Distance estimation
- Safety monitoring

### Phase 5

Intelligent Tracking

- Target selection
- Gimbal tracking
- PID controller

### Phase 6

Edge AI Deployment

- Jetson deployment
- TensorRT
- GPU optimization

### Phase 7

Decision Engine

- Autonomous decision making
- Mission modes
- State management

### Phase 8

Command & Control

- Remote monitoring
- Dashboard
- API integration

---

## 📸 Hardware

Development Machine

- Windows 11
- Ubuntu (WSL2)
- Docker

Deployment Hardware

- NVIDIA Jetson Orin Nano
- Skydroid C12 Thermal + 2K HD Dynamic Tracking Camera
- 3-Axis Gimbal

---

## 📈 Future Improvements

- Thermal and RGB image fusion
- Remote web dashboard
- Multi-camera support
- Face recognition
- Automatic event reporting
- MQTT integration
- Cloud synchronization

---

## 🤝 Contributing

This project is currently being developed as a final-year engineering project.

Suggestions, ideas, and constructive feedback are always welcome.

---

## 📜 License

This repository is intended for educational and research purposes.

---

⭐ If you find this project interesting, feel free to star the repository and follow its progress.
