import serial as serial
import speech_recognition as sr
import time

# Setup serial communication (Change 'COM3' to your Arduino's port, e.g., '/dev/ttyUSB0' for Linux/Mac)
arduino_port = 'COM3'  # Update with your correct port
baud_rate = 9600       # Match the baud rate of your Arduino
ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # Allow time for the connection to initialize

# Initialize speech recognizer
recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("Say 'Red light', 'Green light' or 'End GAME'...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).strip()
            return command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand. Please try again.")
            return None
        except sr.RequestError:
            print("Error connecting to recognition service.")
            return None
        except sr.WaitTimeoutError:
            print("No speech detected, please try again.")
            return None

while True:
    command = recognize_speech()
    
    if command:
        if "red light" in command.lower():
            print("Command: Red light")
            ser.write(b"Red light\n")  # Send command to Arduino
        elif "green light" in command.lower():
            print("Command: Green light")
            ser.write(b"Green light\n")  # Send command to Arduino
        elif "end game" in command.lower():
            print("Command: End game")
            ser.write(b"END GAME\n")  # Send command to Arduino
            print("Game ended. Exiting script...")
            break
        else:
            print("Invalid command. Please say 'Red light' or 'Green light'.")
    time.sleep(1)

# Close the serial connection when done
ser.close()
