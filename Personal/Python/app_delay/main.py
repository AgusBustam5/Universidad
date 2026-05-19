import flet as ft
import urllib.request
import json

def main(page: ft.Page):

    page.title = "Control de Pedal ESP32"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 700

    texto_conexion = ft.Text("Esperando la conexión...", size=16, color=ft.colors.RED)

    valor_estado = ft.Text("-", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE)
    valor_bateria = ft.Text("-", size=18, weight=ft.FontWeight.BOLD)
    valor_sd = ft.Text("-", size=18, weight=ft.FontWeight.BOLD)

    panel_info = ft.Card(
        elevation=5,
        content=ft.Container(
            padding=20,
            width=320,
            content=ft.Column(
                [
                    ft.Row([ft.Icon(ft.icons.SPEED), ft.Text("Telemetria en Vivo", size=20, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Divider(),
                    ft.Row([ft.Text("Modulo Actual:"), valor_estado], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Row([ft.Text("Nivel de Batería:"), valor_bateria], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Row([ft.Text("Memoria SD:"), valor_sd], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                ]
            )
        )
    )

    def actualizar_datos(e):
        texto_conexion.value = "Consultando al ESP32..."
        texto_conexion.color = ft.colors.ORANGE
        page.update()
        try:

            esp32_url = "http://192.168.4.1/api/estado"
            with urllib.request.urlopen(esp32_url, timeout=3) as respuesta:

                if respuesta.status == 200:

                    datos_crudos = respuesta.read().decode("utf-8")
                    datos_json = json.loads(datos_crudos)

                    valor_estado.value = str(datos_json.get("estado", "Error")).capitalize()
                    valor_bateria.value = f"{datos_json.get('bateria', 0)} %"
                    valor_sd.value = str(datos_json.get("tarjeta_sd", "Error")).capitalize()

                    texto_conexion.value = "¡Sincronizado con éxito!"
                    texto_conexion.color = ft.colors.GREEN

                else:
                    texto_conexion.value = f"Error del servidor: {respuesta.status}"
                    texto_conexion.color = ft.colors.RED
        
        except Exception as error:
            texto_conexion.value = f"Fallo de sistema: {str(error)}"
            texto_conexion.color = ft.colors.RED

        page.update()

    boton_actualizar = ft.ElevatedButton(
        text="Sincronizar Pedal",
        icon=ft.icons.SYNC,
        on_click=actualizar_datos,
        scale=1.2,
        bgcolor=ft.colors.BLUE_700,
        color=ft.colors.WHITE
    )

    page.add(
        ft.Icon(ft.icons.SPEAKER_GROUP, size=70, color=ft.colors.BLUE_GREY_800),
        ft.Text("Sistema Híbrido V1", size=26, weight=ft.FontWeight.W_900),
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        panel_info,
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        boton_actualizar,
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        texto_conexion
    )

ft.app(target=main)