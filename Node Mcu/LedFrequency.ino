// Define the pin for the LED
const int ledPin = D6;

// Variable to store the number of blinks per second
float frequency = 1.0;
float previousFrequency = -1.0; // Variable to store the previous frequency

void setup() {
  // Initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);
  
  // Initialize serial communication at 9600 bits per second
  Serial.begin(9600);
  
  // Print instructions to the serial monitor
  Serial.println("Enter frequency:");

  // Print the default frequency value to the serial monitor
  Serial.print("Default frequency set to: ");
  Serial.println(frequency);
  float delayTime = 1000.0 / frequency / 2.0; // Divided by 2 for on and off time
  float delayTimeInSeconds = delayTime / 1000.0;
  
  // Print LED on and off time in seconds
  Serial.print("LED on and off time: ");
  Serial.print(delayTimeInSeconds, 3); // Print with 3 decimal places
  Serial.println(" seconds");
}

void loop() {
  // Check if there is any input from the serial monitor
  if (Serial.available() > 0) {
    // Read the input as a string
    String input = Serial.readString();
    
    // Convert the input string to a float
    frequency = input.toFloat();
    
    // Make sure the number of blinks per second is non-negative
    if (frequency < 0.0) {
      frequency = 0.0;
    }
    
    // Print the received value to the serial monitor
    Serial.print("Frequency set to: ");
    Serial.println(frequency);
  }
  
  // If the frequency has changed, print the delay time in seconds
  if (frequency != previousFrequency) {
    if (frequency > 0.0) {
      float delayTime = 1000.0 / frequency / 2.0; // Divided by 2 for on and off time
      float delayTimeInSeconds = delayTime / 1000.0;
      Serial.print("LED on and off time: ");
      Serial.print(delayTimeInSeconds, 3); // Print with 3 decimal places
      Serial.println(" seconds");
    }
    previousFrequency = frequency;
  }
  
  // If the user entered a valid number, blink the LED accordingly
  if (frequency > 0.0) {
    float delayTime = 1000.0 / frequency / 2.0; // Divided by 2 for on and off time
    
    // Blink the LED on
    digitalWrite(ledPin, HIGH);
    delay(delayTime);
    
    // Blink the LED off
    digitalWrite(ledPin, LOW);
    delay(delayTime);
  }
}
