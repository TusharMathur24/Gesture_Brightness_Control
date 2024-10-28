# Gesture_Brightness_Control
This project is a Python application that controls screen brightness using hand gestures, specifically by calculating the distance between the user's thumb and index finger. The application utilizes OpenCV for video processing, MediaPipe for hand tracking, and WMI (Windows Management Instrumentation) to manage the screen brightness on a Windows machine.

Features
Hand Tracking: Uses MediaPipe's Hand Tracking to detect hand landmarks in real-time.
Brightness Control: Adjusts screen brightness by interpreting the distance between thumb and index finger tips.
Real-Time Video Feedback: Displays the user's camera feed with visual markers to show the brightness control gesture in action.
Requirements
Python 3.6 or later
OpenCV
MediaPipe
WMI (for Windows-based brightness control)
