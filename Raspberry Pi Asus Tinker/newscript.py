'''
by kuldip singh https://github.com/itskuldipsingh/LED-blink-RaspberryPi-Asus-Tinker-Board/tree/main
'''
import ASUS.GPIO as GPIO
import time
import threading
import math

def mode1():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    LED1 = 11
    GPIO.setup(LED1, GPIO.OUT)

    Frequency1 = 1.0  # Default Frequency
    TimePeriod1 = 1 / Frequency1
    GlowTime1 = TimePeriod1 / 2
    DarkTime1 = TimePeriod1 / 2

    def print_default_values1():
        if Frequency1 == 0:
            print("Glow Time: Infinite \t Dark Time: {:.6f} seconds \t Time Period: Infinite \t Frequency: {:.6f} Hz".format(DarkTime1, Frequency1))
        else:
            print("Glow Time: {:.6f} seconds \t Dark Time: {:.6f} seconds \t Time Period: {:.6f} seconds \t Frequency: {:.6f} Hz".format(GlowTime1, DarkTime1, TimePeriod1, Frequency1))

    def blink_led1():
        while True:
            GPIO.output(LED1, GPIO.HIGH)
            if math.isinf(GlowTime1):  # Check if GlowTime is infinite
                time.sleep(0.1)  # Adjust the sleep duration as needed
                continue
            time.sleep(GlowTime1)

            GPIO.output(LED1, GPIO.LOW)
            time.sleep(DarkTime1)

    def get_user_input1():
        nonlocal Frequency1, TimePeriod1, GlowTime1, DarkTime1
        while True:
            try:
                new_Frequency1 = float(input("Enter frequency in Hz: "))

                if new_Frequency1 > 0:
                    Frequency1 = new_Frequency1
                    TimePeriod1 = 1 / Frequency1
                    GlowTime1 = TimePeriod1 / 2
                    DarkTime1 = TimePeriod1 / 2
                    print_default_values1()
                elif new_Frequency1 == 0:
                    Frequency1 = new_Frequency1
                    TimePeriod1 = float('inf')  # Representing infinity for TimePeriod
                    GlowTime1 = float('inf')  # Representing infinity for GlowTime
                    DarkTime1 = 0
                    print_default_values1()
                else:
                    print("Invalid input. Please enter non-negative values for frequency.")
            except ValueError:
                print("Invalid input. Please enter numeric values for frequency.")

    try:
        GPIO.output(LED1, GPIO.HIGH)  # Turn LED on initially
        print_default_values1()

        blinking_thread = threading.Thread(target=blink_led1)
        blinking_thread.start()

        input_thread = threading.Thread(target=get_user_input1)
        input_thread.start()

        input_thread.join()

    except KeyboardInterrupt:
        GPIO.cleanup()

def mode2():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    LED2 = 11
    GPIO.setup(LED2, GPIO.OUT)

    GlowTime2 = 0.5  # Default Glow Time
    DarkTime2 = 0.5  # Default Dark Time
    TimePeriod2 = GlowTime2 + DarkTime2
    Frequency2 = 1/TimePeriod2

    def print_default_values2():
        print("Glow Time: {:.6f} seconds \t Dark Time: {:.6f} seconds \t Time Period: {:.6f} seconds \t Frequency: {:.6f} Hz".format(GlowTime2, DarkTime2, TimePeriod2, Frequency2))

    def blink_led2():
        while True:
            GPIO.output(LED2, GPIO.HIGH)
            time.sleep(GlowTime2)

            GPIO.output(LED2, GPIO.LOW)
            time.sleep(DarkTime2)

    def get_user_input2():
        nonlocal GlowTime2, DarkTime2, TimePeriod2, Frequency2
        while True:
            try:
                new_glow_time2 = float(input("Enter Glow Time in seconds: "))
                new_dark_time2 = float(input("Enter Dark Time in seconds: "))

                if new_glow_time2 >= 0 and new_dark_time2 >= 0:
                    GlowTime2 = new_glow_time2
                    DarkTime2 = new_dark_time2
                    TimePeriod2 = GlowTime2 + DarkTime2
                    Frequency2 = 1/TimePeriod2
                    print_default_values2()
                else:
                    print("Invalid input. Please enter non-negative values for Glow Time and Dark Time.")
            except ValueError:
                print("Invalid input. Please enter numeric values for Glow Time and Dark Time.")

    try:
        GPIO.output(LED2, GPIO.HIGH)  # Turn LED on initially
        print_default_values2()

        blinking_thread = threading.Thread(target=blink_led2)
        blinking_thread.start()

        input_thread = threading.Thread(target=get_user_input2)
        input_thread.start()

        input_thread.join()

    except KeyboardInterrupt:
        GPIO.cleanup()

def get_user_input():
    while True:
        try:
            mode = int(input("Select mode (1 for Frequency and 2 for Bright and Dark time): "))

            if mode == 1:
                mode1()
            elif mode == 2:
                mode2()
            else:
                print("Invalid mode. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

try:
    get_user_input()

except KeyboardInterrupt:
    GPIO.cleanup()
