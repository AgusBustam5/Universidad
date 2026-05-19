import flet as ft
import urllib.request
import json
import asyncio

def main(page: ft.Page):
    
    page.title = "Control de Pedal ESP32"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    texto_conexion = ft.Text("Esperando la conexión...", size=16, color=ft.Colors.RED)

    valor_estado = ft.Text("-", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
    valor_bateria = ft.Text("-", size=18, weight=ft.FontWeight.BOLD)
    valor_sd = ft.Text("-", size=18, weight=ft.FontWeight.BOLD)

    panel_info = ft.Card(
        elevation=5,
        content=ft.Container(
            padding=20,
            width=320,
            content=ft.Column(
                [
                    ft.Row([ft.Icon("speed"), ft.Text("Telemetria en Vivo", size=20, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Divider(),
                    ft.Row([ft.Text("Modulo Actual:"), valor_estado], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Row([ft.Text("Nivel de Batería:"), valor_bateria], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Row([ft.Text("Memoria SD:"), valor_sd], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                ]
            )
        )
    )

    async def actualizar_datos(e):
        texto_conexion.value = "Consultando al ESP32..."
        texto_conexion.color = ft.Colors.ORANGE
        page.update()

        def tarea_red(e):
            try:

                esp32_url = "http://192.168.4.1/api/estado"
                with urllib.request.urlopen(esp32_url, timeout=3) as respuesta:

                    if respuesta.status == 200:

                        datos_crudos = respuesta.read().decode("utf-8")
                        datos = json.loads(datos_crudos)
                        return datos, None

                    return None, f"Error {respuesta.status}"

            except Exception as error:
                return None, str(error)

        loop = asyncio.get_event_loop()
        datos_json, error = await loop.run_in_excexutor(None, tarea_red)

        if datos_json:
            valor_estado.value = str(datos_json.get("estado", "Error")).capitalize()
            valor_bateria.value = f"{datos_json.get('bateria', 0)} %"
            valor_sd.value = str(datos_json.get("tarjeta_sd", "Error")).capitalize()
            texto_conexion.value = "¡Sincronizado con éxito!"
            texto_conexion.color = ft.Colors.GREEN
    
        else:
            texto_conexion.value = f"Fallo: {error}"
            texto_conexion.color = ft.Colors.RED
    
        page.update()

    boton_actualizar = ft.ElevatedButton(
        width=260,
        height=55,
        content=ft.Row(
            [ft.Icon("sync"), ft.Text("Sincronizar Pedal")],
            alignment=ft.MainAxisAlignment.CENTER 
        ),
        on_click=actualizar_datos,
        scale=1.2,
        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE
    )

    page.add(
        ft.Icon("speaker_group", size=70, color=ft.Colors.BLUE_GREY_800),
        ft.Text("Sistema Híbrido V1", size=26, weight=ft.FontWeight.W_900),
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        panel_info,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        boton_actualizar,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        texto_conexion
    )

ft.app(target=main)