# Gesture Brightness Control
Gesture_Brightness_Control is a Python project that enables users to control the brightness of their screen through simple hand gestures. Using OpenCV and MediaPipe, this program captures hand movements in real time via the webcam and adjusts the brightness based on the distance between the user's thumb and index finger.

How It Works
The project leverages MediaPipe's Hand module to detect and track hand landmarks, specifically focusing on the thumb and index fingertips. By measuring the distance between these two points, the program translates this distance into a brightness level for the screen. The brightness is then set using the Windows Management Instrumentation (WMI) interface.

Key Features
Real-time Hand Detection: Uses MediaPipe to detect hand landmarks in real time.
Brightness Control: Maps the distance between thumb and index finger to adjust screen brightness.
Visual Feedback: Displays brightness percentage and graphical indicators for the current brightness level.

Prerequisites
Python 3.x
OpenCV (cv2)
MediaPipe (mediapipe)
WMI (wmi)
