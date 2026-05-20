#include "web_server.h"
#include "file_manager.h"
#include <ArduinoJson.h>
#include <LittleFS.h>

AsyncWebServer server(80);

const char manifest_json[] PROGMEM = R"rawliteral(
{
    "name": "Control de Pedal ESP32",
    "short_name": "Pedal V1",
    "start_url" : "/",
    "display": "standalone",
    "background_color": "#121212",
    "theme_color": "#121212",
    "icons": [
        {
            "src": "/icon.png",
            "sizes": "192x192 512x512",
            "type": "image/svg+xml"
            }]
}
)rawliteral";

const char sw_js[] PROGMEM = "self.addEventListener('fetch', function(event) {})";

const char pagina_html[] PROGMEM = R"rawliteral(
<!DOCTYPE html>
<html>
<head>
    <meta charset¨"UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="manifest" href="/manifest.json">
    <style>
        :root {
            --bg-color: #0f0f12;
            --card-bg: #1e1e24;
            --accent: #ff3e3e; /* Color rojo eléctrico para el pedal */
            --text: #ffffff;
        }
        body { 
            font-family: 'Segoe UI', Roboto, sans-serif; 
            background-color: var(--bg-color); 
            color: var(--text); 
            margin: 0; 
            padding: 0;
        }
        h1 { font-weight: 300; letter-spacing: 2px; margin-top: 20px; }

        .tab-content { padding: 20px; display: none; }
        .tab-content.active { display: block; }

        /* Estilo de Tarjeta para la lista */
        .file-card { 
            background: var(--card-bg); 
            border-radius: 15px; 
            padding: 15px; 
            margin: 10px 0; 
            display: flex; 
            align-items: center; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }

        /* Botones estilo pedal */
        .btn {
            background: var(--accent);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 25px;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(255, 62, 62, 0.3);
            transition: transform 0.2s;
        }
        .btn:active { transform: scale(0.95); }

        .nav-bar { 
            position: fixed; bottom: 0; width: 100%; 
            background: #1a1a1f; display: flex; 
            border-top: 1px solid #333;
        }
        .nav-btn { flex: 1; padding: 15px; border: none; background: none; color: #666; }
        .nav-btn.active { color: var(--accent); }
    </style>
</head>
<body>
    <div id="home" class="tab-content active">
        <h1>Pedal ESP32</h1>
        <button onclick="sincronizar()">Consultar Estado</button>
        <p id="status">Esperando...</p>
    </div>

    <div id="sd-files" class="tab-content">
        <h1>Archivos WAV</h1>
        <button class="btn" onclick="cargarWavs()">REFRESCAR LISTA</button>
        <div id="lista-wavs" style="margin-top: 20px;"></div>
    </div>

    <div class="nav-bar">
        <button class="nav-btn active" onclick="showTab('home', this)">Inicio</button>
        <button class="nav-btn" onclick="showTab('sd-files', this)">Archivos</button>
    </div>

    <script>
        function showTab(tabId, btn) {
            document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            btn.classList.add('active');
        }

        async function cargarWavs() {
            let res = await fetch("/api/wavs");
            let data = await res.json();
            let lista = document.getElementById("lista-wavs");

            lista.innerHTML = data.map(f => `
                <div class="file-card">
                    <span style="font-size: 24px; margin-right: 15px;">&#127925</span>
                    <div>
                        <div style="font-weight: bold;">${f}</div>
                        <div style="font-size: 12px; color: #888;">Archivo de Audio</div>
                    </div>
                </div>
            `).join('');
        }
    </script>
</body>
</html>
)rawliteral";

void initWebServer() {
    server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
        request->send(200, "text/html", pagina_html);
    });

    server.on("/icon.png", HTTP_GET, [](AsyncWebServerRequest *request){
    Serial.println("Entregando logo custom...");
    request->send(LittleFS, "/icon.png", "image/png");
  });

    server.on("/api/estado", HTTP_GET, [](AsyncWebServerRequest *request){
        StaticJsonDocument<200> doc;
        doc["estado"] = "operativo";
        String output;
        serializeJson(doc, output);
        request->send(200, "application/json", output);
    });

    server.on("/manifest.json", HTTP_GET, [](AsyncWebServerRequest *request){
        request->send_P(200, "application/json", manifest_json);
    });

    server.on("/sw.js", HTTP_GET, [](AsyncWebServerRequest *request){
    Serial.println("Samsung pidio el Service Worker...");
    request->send_P(200, "application/javascript", sw_js);
  });
    server.on("/api/wavs", HTTP_GET, [](AsyncWebServerRequest *request){
        request->send(200, "application/json; charset=utf-8", getWavFilesAsJson());
    });

    server.begin();

}