#include <Arduino.h>
#include <WiFi.h>
#include <ESPAsyncWebServer.h>
#include <ArduinoJson.h>

const char *ssid = "Pedal_WiFi";
const char *password = "Churroaluca";

AsyncWebServer server(80);

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("\n---Despertando ESP32. Iniciando Antena Wi-Fi ---");

  Serial.println("... Confgurando la red ...");
  WiFi.softAP(ssid, password);

  IPAddress myIP = WiFi.softAPIP();

  Serial.println("¡Red Wi-Fi creada con éxito!");
  Serial.print("Busca la red en tu celular:");
  Serial.println(ssid);
  Serial.print("Mi direccion IP es: ");
  Serial.println(myIP);
  Serial.println("\nEsperando a que te conectes...");

  server.on("/", HTTP_GET, [](AsyncWebServerRequest * request){
    Serial.println("Celular detectado por el servidor!");

    StaticJsonDocument<200> doc;
    doc["estado"] = "listo";
    doc["bateria"] = 85;
    doc["tarjeta_sd"] = "conectada";

    String respuesta_json;
    serializeJson(doc, respuesta_json);

    request->send(200, "text/plain", "¡Hola desde tu pedal ESP32! El servidor se encuentra listo para transferir pistas.");
  });

  server.begin();
  Serial.println("Servidor Web asincronico en linea y esperando...");
}

void loop() {

  delay(1000);
}