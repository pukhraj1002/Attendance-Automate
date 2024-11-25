# Face Recognition Attendance System

A Python-based face recognition attendance system that uses a webcam to detect and recognize individuals from pre-fed images and marks their attendance in an Excel file.

---

## Features

- **Face Detection:** Detects faces in real-time using a webcam.
- **Face Recognition:** Matches detected faces with pre-fed images.
- **Attendance Recording:** Logs recognized individuals' names with timestamps in an Excel file.
- **Real-Time Visualization:** Draws rectangles around detected faces and displays names.

---

## Demo

### Real-time Detection and Recognition:
![Demo Screenshot](demo-screenshot.png)

### Attendance Record Example:
| Name      | Time                |
|-----------|---------------------|
| Pukhraj   | 2024-11-25 10:30 AM |

---

## Requirements

Ensure the following are installed:
- Python 3.8 or higher
- A functional webcam

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/face-recognition-attendance.git
   cd face-recognition-attendance

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

2. **Run the Scripts:**
   ```bash
   python attendance_system.py
