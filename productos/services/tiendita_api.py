import requests
import os
from django.core.exceptions import ValidationError

TIENDITA_ENDPOINT = os.getenv('TIENDITA_ENDPOINT', 'https://tiendita.example.com/api/productos/')
TIENDITA_TOKEN = os.getenv('TIENDITA_TOKEN', 'tu_token_aqui')

def enviar_producto(producto):
    headers = {
        'Authorization': f'Token {TIENDITA_TOKEN}',
    }

    with open(producto['imagen'], 'rb') as img_file:
        files = {
            'image': (os.path.basename(producto['imagen']), img_file, 'image/jpeg'),
        }
        data = {
            'nombre': producto['nombre'],
            'descripcion': producto['descripcion'],
            'precio': producto['precio'],
            'stock': producto['stock'],
        }

        response = requests.post(TIENDITA_ENDPOINT, headers=headers, data=data, files=files)

    if response.status_code != 201:
        raise ValidationError(f"Error al enviar producto: {response.status_code} - {response.text}")

    return response.json()
