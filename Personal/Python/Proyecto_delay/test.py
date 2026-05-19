import requests

esp32_url = "http://192.168.4.1/"

try:
    print("Buscando al ESP32...")
    respuesta = requests.get(esp32_url)

    if respuesta.status_code == 200:
        print("Conexion exitosa. El ESP32 dice:")
        print(respuesta.text)
    
    else:
        print(f"Error al conectar: {respuesta.status_code}")

except Exception as e:
    print(f"No fue posible la conexion. ¿Estas bien conectado al WiFi? Error: {e}")