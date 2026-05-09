#include <Arduino.h>

// Definir pin visual
const int pinLED = 2;
// variables metronomo
int bpm = 60;
int intervaloDeGolpe = 1000;

TaskHandle_t TareaVisual;

// --- Tarea Visual ---
void metronomoVisual(void * parameter) {
  for(;;) {
    // Parpadeo LED
    digitalWrite(pinLED, HIGH);
    vTaskDelay(50 / portTICK_PERIOD_MS);
    digitalWrite(pinLED, LOW);

    // Esperar golpe siguiente
    vTaskDelay((intervaloDeGolpe - 50) / portTICK_PERIOD_MS);
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(pinLED, OUTPUT);

  Serial.println("Metronomo Iniciado");
  Serial.println("Puedes escribir un numero para cambiar los BPM");

  // Asignar tarea visual al nucleo 0
  xTaskCreatePinnedToCore(
    metronomoVisual,
    "Tarea_LED",
    1000,
    NULL,
    1,
    &TareaVisual,
    0);
}

void loop() {
  // Revisar Input
  if (Serial.available() > 0) {
    int nuevoBPM = Serial.parseInt();

    // Validar que sea un ritmo rasonable
    if (nuevoBPM >= 30 && nuevoBPM <= 200) {
      bpm = nuevoBPM;
      intervaloDeGolpe = 60000 / bpm;

      Serial.print(">>> Ritmo Ajustado ");
      Serial.print(bpm);
      Serial.println(" BPM");
    }
  }
  // put your main code here, to run repeatedly:
  vTaskDelay(100 / portTICK_PERIOD_MS); // this speeds up the simulation
}
