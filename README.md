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
Installation
Clone this repository:

bash
Copy code
git clone https://github.com/your_username/Gesture_Brightness_Control.git
cd Gesture_Brightness_Control
Install the required libraries:

bash
Copy code
pip install opencv-python mediapipe wmi numpy
Ensure you have a working camera on your computer, as the application uses it to detect hand gestures.

Usage
Run the Python script:

bash
Copy code
python gesture_brightness_control.py
Use your thumb and index finger to control the brightness:

Bring your thumb and index finger close to lower the brightness.
Spread them apart to increase the brightness.
Press 'q' to exit the application.

Code Explanation
The main components of this project include:

Hand Detection: MediaPipe’s Hands module is used to detect hand landmarks.
Brightness Calculation: The distance between the thumb and index finger tips is used to calculate a brightness level (mapped from 0 to 100%).
Real-Time Display: OpenCV displays the video feed with visual indicators for the brightness bar and landmarks.
Example
On starting the application, the webcam feed will open. Move your thumb and index finger together or apart to control brightness, as shown below.

Gesture	Brightness Adjustment
Thumb and index close	Decrease Brightness
Thumb and index far apart	Increase Brightness
Troubleshooting
WMI Not Available: This project currently only supports Windows.
Brightness Not Changing: Ensure the script is running with sufficient privileges to adjust screen brightness.
License
This project is open-source and available under the MIT License.
