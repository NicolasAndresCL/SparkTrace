import requests
from productos.excepciones import APIError

def enviar_productos_a_tiendita(productos):
    url = "https://api.tiendita.com/productos"
    response = requests.post(url, json=productos)

    if response.status_code != 200:
        try:
            detalle = response.json().get("error", "Sin detalle")
        except Exception:
            detalle = "Respuesta no procesable"
        raise APIError(f"{detalle}", response.status_code)

    return response.json()
