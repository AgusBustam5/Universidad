#include <Arduino.h>
#include <WiFi.h>
#include <LittleFS.h>
#include "config.h"
#include "web_server.h"
#include "file_manager.h"

void setup() {
  Serial.begin(115200);

  if(!LittleFS.begin(true)){
    Serial.println("Error al montar LittleFS");
    return;
  }

  initSD();

  Serial.println("\n---Iniciando Antena Wi-Fi ---");
  WiFi.softAP(ssid, password);
  Serial.println("Red Cread:  " + String(ssid));
  Serial.println("IP: " + WiFi.softAPIP().toString());
  
  initWebServer();
  Serial.println("Servidor Web asincronico en linea y esperando...");
}

void loop() {

  delay(1000);
}