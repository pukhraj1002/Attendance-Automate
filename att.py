import cv2
import face_recognition
import os
import pandas as pd
import datetime

# Path to the folder containing pre-fed images
KNOWN_FACES_DIR = "C:/Users/Pukhraj/Desktop/Things/Demo/attendance/Photo"

# Load known faces and names
known_face_encodings = []
known_face_names = []

print("Loading known faces...")
for file_name in os.listdir(KNOWN_FACES_DIR):
    file_path = os.path.join(KNOWN_FACES_DIR, file_name)
    # Ensure it's an image file
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        image = face_recognition.load_image_file(file_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_face_encodings.append(encodings[0])
            known_face_names.append(os.path.splitext(file_name)[0])  # Use file name (without extension) as the name
        else:
            print(f"Warning: No face found in {file_name}, skipping.")

# Create a DataFrame for attendance
attendance_df = pd.DataFrame(columns=["Name", "Time"])

# Function to mark attendance
def mark_attendance(name):
    global attendance_df
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if name not in attendance_df["Name"].values:
        attendance_df = attendance_df.append({"Name": name, "Time": current_time}, ignore_index=True)
        print(f"Attendance marked for {name}")

# Initialize webcam
cap = cv2.VideoCapture(0)

print("Press 'q' to quit and save attendance.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces and their encodings in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compare detected face with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_face_names[match_index]

        # Mark attendance
        mark_attendance(name)

        # Scale face location back to original frame size
        top, right, bottom, left = [v * 4 for v in face_location]

        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Show video feed
    cv2.imshow("Attendance System", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Save the attendance to an Excel file
file_name = f"attendance_{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.xlsx"
attendance_df.to_excel(file_name, index=False)
print(f"Attendance saved to {file_name}")
