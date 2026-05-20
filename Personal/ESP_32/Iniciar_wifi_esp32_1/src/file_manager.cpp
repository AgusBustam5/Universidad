#include "file_manager.h"
#include <ArduinoJson.h>

void initSD() {
    if(!SD.begin(5)){
        Serial.println("Error: No se detectó tarjeta SD");
    } else {
        Serial.println("Tarjeta SD lista.");
    }
}

String getWavFilesAsJson() {
    DynamicJsonDocument doc(2048);
    JsonArray array = doc.to<JsonArray>();

    //Temporal
    if(!SD.begin(5)) {
        array.add("demo_delay.wav");
        array.add("prueba_eco.wav");
        array.add("sintetizador.wav");
    } else {
        File root = SD.open("/");
        if(root) {
            File file = root.openNextFile();
            while(file) {
                if(!file.isDirectory()) {
                    String nombre = String(file.name());
                    if(nombre.endsWith(".wav") || nombre.endsWith(".WAV")){
                        array.add(nombre);
                    }
                }
                file = root.openNextFile();
            }
            root.close();
        }
    }
    String output;
    serializeJson(doc, output);
    return output;
}