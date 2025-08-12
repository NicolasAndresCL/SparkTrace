import pytest
from unittest.mock import patch
from pathlib import Path
import json

from productos.integraciones.tiendita import enviar_productos_a_tiendita
from productos.excepciones import APIError

def cargar_fixture(nombre):
    ruta = Path(__file__).resolve().parent / "mocks" / nombre
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)
@patch("productos.integraciones.tiendita.requests.post")
def test_envio_exitoso_con_fixture(mock_post):
    productos = cargar_fixture("productos_validos.json")
    respuesta_simulada = cargar_fixture("respuesta_api_exitosa.json")

    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = respuesta_simulada

    respuesta = enviar_productos_a_tiendita(productos)
    assert respuesta["status"] == "ok"
    assert respuesta["recibidos"] == len(productos)

@patch("productos.integraciones.tiendita.requests.post")
def test_envio_falla_con_fixture(mock_post):
    productos = cargar_fixture("productos_invalidos.json")
    respuesta_error = cargar_fixture("respuesta_api_error.json")

    mock_post.return_value.status_code = 500
    mock_post.return_value.json.return_value = respuesta_error

    with pytest.raises(APIError) as exc:
        enviar_productos_a_tiendita(productos)

    assert "Falla interna" in str(exc.value)
    assert exc.value.status_code == 500

@patch("productos.integraciones.tiendita.requests.post")
def test_envio_con_productos_vacios(mock_post):
    productos = cargar_fixture("productos_vacios.json")
    respuesta_error = cargar_fixture("respuesta_lista_vacia.json")

    mock_post.return_value.status_code = 400
    mock_post.return_value.json.return_value = respuesta_error

    with pytest.raises(APIError) as exc:
        enviar_productos_a_tiendita(productos)

    assert "Lista vacía" in str(exc.value)
    assert exc.value.status_code == 400


@patch("productos.integraciones.tiendita.requests.post")
def test_envio_con_campos_faltantes(mock_post):
    productos = cargar_fixture("productos_sin_precio.json")
    respuesta_error = cargar_fixture("respuesta_faltante_precio.json")

    mock_post.return_value.status_code = 422
    mock_post.return_value.json.return_value = respuesta_error

    with pytest.raises(APIError) as exc:
        enviar_productos_a_tiendita(productos)

    assert "precio" in str(exc.value)
    assert exc.value.status_code == 422

@patch("productos.integraciones.tiendita.requests.post")
def test_respuesta_inesperada(mock_post):
    productos = cargar_fixture("productos_validos.json")

    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = None  # Simula respuesta vacía

    respuesta = enviar_productos_a_tiendita(productos)
    assert respuesta is None  # O puedes validar que se maneje como error si prefieres

