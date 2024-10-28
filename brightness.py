import cv2
import mediapipe as mp
import numpy as np
import wmi

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

c = wmi.WMI(namespace='wmi')
brightness_methods = c.WmiMonitorBrightnessMethods()[0]
brightness_levels = c.WmiMonitorBrightness()[0]
current_brightness = brightness_levels.CurrentBrightness
min_brightness = 0
max_brightness = 100

brightness_bar = 400
brightness_percentage = current_brightness

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_lms.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])
                
            if lm_list:
                thumb_tip = lm_list[4]
                index_tip = lm_list[8]
                
                x1, y1 = thumb_tip[1], thumb_tip[2]
                x2, y2 = index_tip[1], index_tip[2]
                length = np.hypot(x2 - x1, y2 - y1)
                
                brightness_percentage = np.interp(length, [20, 200], [min_brightness, max_brightness])
                brightness_bar = np.interp(length, [20, 200], [400, 150])
                brightness_methods.WmiSetBrightness(int(brightness_percentage), 0)  
                
                cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(brightness_bar)), (85, 400), (0, 255, 0), cv2.FILLED)

    cv2.putText(img, f'{int(brightness_percentage)} %', (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Gesture Brightness Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
