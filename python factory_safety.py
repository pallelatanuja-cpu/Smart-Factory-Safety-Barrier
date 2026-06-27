import cv2
import serial
import time

# CRUCIAL: Change 'COM5' to your exact port number from the Arduino IDE
arduino_port = 'COM5' 

try:
    arduino = serial.Serial(port=arduino_port, baudrate=9600, timeout=.1)
    time.sleep(2) # Give Arduino time to reset and establish connection
    print(f"Connected successfully to Arduino on {arduino_port}")
except:
    print(f"ERROR: Could not connect to {arduino_port}. Check your port number!")
    exit()

# Initialize your built-in laptop camera
cap = cv2.VideoCapture(0)

print("\n--- System Active ---")
print("Hold a bright RED object in front of your camera to trigger the safety gate.")
print("Press the 'q' key on your keyboard while focusing on the video screen to close.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab camera frame.")
        break

    # Convert the video frame from standard BGR color to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define range of red color in HSV spectrum
    lower_red = (0, 120, 70)
    upper_red = (10, 255, 255)
    
    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Count how many pixels in the frame are red
    red_pixel_count = cv2.countNonZero(mask)
    
    # If more than 8000 pixels are red, trigger the hazard response
    if red_pixel_count > 8000: 
        cv2.putText(frame, "DANGER: HAZARD DETECTED", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        arduino.write(b'1') # Send byte '1' to Arduino
    else:
        cv2.putText(frame, "SYSTEM STATUS: SAFE", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        arduino.write(b'0') # Send byte '0' to Arduino

    # Display the live window
    cv2.imshow("Smart Factory Camera Feed", frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
print("System disconnected safely.")