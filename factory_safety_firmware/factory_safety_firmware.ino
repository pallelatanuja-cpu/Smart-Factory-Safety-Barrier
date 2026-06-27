#include <Servo.h>

Servo safetyGate;
const int buzzerPin = 8; // Buzzer connected to Digital Pin 8

void setup() {
  Serial.begin(9600);        // Initialize USB communication at 9600 speed
  safetyGate.attach(9);      // Servo motor signal wire connected to Pin 9
  pinMode(buzzerPin, OUTPUT);
  safetyGate.write(0);       // Move gate to starting position (0 degrees)
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the character sent from Python
    
    if (command == '1') {         // Danger detected
      digitalWrite(buzzerPin, HIGH); // Sound the buzzer
      safetyGate.write(90);          // Rotate servo to 90 degrees (Drop Gate)
    } 
    else if (command == '0') {    // Area is safe
      digitalWrite(buzzerPin, LOW);  // Turn off the buzzer
      safetyGate.write(0);           // Rotate servo back to 0 degrees (Open Gate)
    }
  }
}