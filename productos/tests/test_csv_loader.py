import pytest
import tempfile
import os
from productos.utils.csv_loader import cargar_productos_desde_csv
from django.core.exceptions import ValidationError

def crear_csv_valido(ruta_csv, ruta_imagen):
    with open(ruta_csv, 'w', encoding='utf-8') as f:
        f.write(f"nombre,descripcion,precio,stock,image\n")
        f.write(f"Pelota,Juguete redondo,4990,10,{ruta_imagen}\n")

def test_carga_valida_csv(tmp_path):
    ruta_imagen = tmp_path / "pelota.jpg"
    ruta_imagen.write_bytes(b"fake image data")

    ruta_csv = tmp_path / "productos.csv"
    crear_csv_valido(ruta_csv, ruta_imagen)

    productos = cargar_productos_desde_csv(str(ruta_csv))
    assert len(productos) == 1
    assert productos[0]["nombre"] == "Pelota"

def test_csv_con_precio_invalido(tmp_path):
    ruta_imagen = tmp_path / "pelota.jpg"
    ruta_imagen.write_bytes(b"fake image")

    ruta_csv = tmp_path / "productos.csv"
    with open(ruta_csv, 'w', encoding='utf-8') as f:
        f.write("nombre,descripcion,precio,stock,image\n")
        f.write(f"Pelota,Juguete,abc,10,{ruta_imagen}\n")

    with pytest.raises(ValidationError):
        cargar_productos_desde_csv(str(ruta_csv))
