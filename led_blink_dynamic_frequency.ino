#define LED_BUILTIN 13

float frequency = 1.0;
float timeperiod;
float glowtime;
float darktime;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  calculateTiming();  // Initial calculation of timing values
  //Serial.println("Enter 'q' to quit.");
}

void loop() {
  while (true) {  // Ensure a semicolon here
    // Check if there's new input from the Serial Monitor
    if (Serial.available() > 0) {
      String newfrequency = Serial.readStringUntil('\n');
      newfrequency.trim();

      if (newfrequency.length() > 0) {
        // If input is not empty, update frequency and timing values
        if (newfrequency.toFloat()) {
          frequency = newfrequency.toFloat();
          calculateTiming();
          printValues();
          
        } else {
          Serial.println("Invalid input. Frequency unchanged.");
        }
      } else if (newfrequency == "q") {
        Serial.println("Program terminated.");
        break;  // Now within a valid loop structure
      }
    }

    // Blink the LED
    digitalWrite(LED_BUILTIN, HIGH);
    delay((unsigned long)(glowtime * 1000));  // Convert to milliseconds
    digitalWrite(LED_BUILTIN, LOW);
    delay((unsigned long)(darktime * 1000));  // Convert to milliseconds
  }
}

void calculateTiming() {
  timeperiod = 1.0 / frequency;
  glowtime = timeperiod / 2.0;
  darktime = glowtime;
}

void printValues() {
  Serial.println("Frequency updated successfully!");
  Serial.print("Frequency: ");
  Serial.print(frequency);
  Serial.print(" Hz, Timeperiod: ");
  Serial.print(timeperiod * 1000); // Convert to milliseconds
  Serial.print(" ms, Glowtime: ");
  Serial.print(glowtime * 1000);    // Convert to milliseconds
  Serial.print(" ms, Darktime: ");
  Serial.print(darktime * 1000);    // Convert to milliseconds
  Serial.println(" ms");
}
