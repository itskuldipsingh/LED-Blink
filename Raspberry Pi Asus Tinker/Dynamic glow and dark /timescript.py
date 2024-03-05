'''
comment 5th line (import ASUS.GPIO as GPIO) and uncomment 6th line (import RPi.GPIO as GPIO) if you are using Raspberry Pi
comment 6th line (import RPi.GPIO as GPIO) and uncomment 5th line (import ASUS.GPIO as GPIO) if you are using ASUS Tinker Board
'''
#import ASUS.GPIO as GPIO
import RPi.GPIO as GPIO

import time
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED = 11
GPIO.setup(LED, GPIO.OUT)

GlowTime = 0.5  # Default Glow Time
DarkTime = 0.5  # Default Dark Time
TimePeriod = GlowTime + DarkTime
Frequency = 1/TimePeriod

def print_default_values():
    print("Glow Time: {:.6f} seconds \t Dark Time: {:.6f} seconds \t Time Period: {:.6f} seconds \t Frequency: {:.6f} Hz".format(GlowTime, DarkTime, TimePeriod, Frequency))

def blink_led():
    global GlowTime, DarkTime
    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(GlowTime)

        GPIO.output(LED, GPIO.LOW)
        time.sleep(DarkTime)

def get_user_input():
    global GlowTime, DarkTime, TimePeriod, Frequency
    while True:
        try:
            new_glow_time = float(input("Enter Glow Time in seconds: "))
            new_dark_time = float(input("Enter Dark Time in seconds: "))

            if new_glow_time >= 0 and new_dark_time >= 0:
                GlowTime = new_glow_time
                DarkTime = new_dark_time
                TimePeriod = GlowTime + DarkTime
                Frequency = 1/TimePeriod
                print_default_values()
            else:
                print("Invalid input. Please enter non-negative values for Glow Time and Dark Time.")
        except ValueError:
            print("Invalid input. Please enter numeric values for Glow Time and Dark Time.")

try:
    GPIO.output(LED, GPIO.HIGH)  # Turn LED on initially
    print_default_values()

    blinking_thread = threading.Thread(target=blink_led)
    blinking_thread.start()

    input_thread = threading.Thread(target=get_user_input)
    input_thread.start()

    input_thread.join()

except KeyboardInterrupt:
    GPIO.cleanup()
