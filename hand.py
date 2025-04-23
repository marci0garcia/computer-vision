import cv2
import mediapipe as mp
import numpy as np

#initialize mediapipe hands and drawing modules
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

#initialize the video caputure
cap = cv2.VideoCapture(0)

#Configure Mediapipe Hands
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame. Exiting...")
            break


    #Flop the frame horizontally for a mirror-like effect
    frame = cv2.flip(frame,1)

    #convert the frame from BGR to RGB (required by mediapipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb_frame = np.ascontinguousarry(rgb_frame, dtype= np.uint8) # Ensure correct dtype

    #Process the frame with Mediapipe hands
    reseult = hands.process(rgb_frame)

    #draw hand landmakrs if detected
    if result.multi_hand_landmarks:
        for hand_landmakrs in result.multi_hand_landmarks:
            #Draw the hand landmarks and connections
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp.hands.HAND_CONNECTIONS)
            
            #display the frame
            cv2.imshow("Hand detection", frame)

            #break the loop if 'q' is pressed
            if cv2.waitKey(1) & oxFF == ord('q'):
                break
    
    #Release the video capture and close windows
    cap.release()
    cv2.destroyAllWindows()
