#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.print("Chip Model: ");
  Serial.println(ESP.getChipModel());
  Serial.print("Chip Revision: ");
  Serial.println(ESP.getChipRevision());
  Serial.println("Hola desde el ESP32");
}

void loop() {}