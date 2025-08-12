import csv
import os
from django.core.exceptions import ValidationError

CAMPOS_OBLIGATORIOS = ['nombre', 'descripcion', 'precio', 'stock', 'image']

def cargar_productos_desde_csv(ruta_csv):
    if not os.path.exists(ruta_csv):
        raise FileNotFoundError(f"Archivo no encontrado: {ruta_csv}")

    productos = []
    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            producto = validar_fila(fila)
            productos.append(producto)
    return productos

def validar_fila(fila):
    for campo in CAMPOS_OBLIGATORIOS:
        if campo not in fila or not fila[campo].strip():
            raise ValidationError(f"Campo obligatorio faltante: {campo}")

    try:
        precio = float(fila['precio'])
        if precio <= 0:
            raise ValidationError("El precio debe ser mayor a cero")
    except ValueError:
        raise ValidationError("Precio inválido")

    try:
        stock = int(fila['stock'])
        if stock < 0:
            raise ValidationError("El stock no puede ser negativo")
    except ValueError:
        raise ValidationError("Stock inválido")

    ruta_imagen = fila['image'].strip()
    if not os.path.exists(ruta_imagen):
        raise ValidationError(f"Imagen no encontrada: {ruta_imagen}")

    return {
        'nombre': fila['nombre'].strip(),
        'descripcion': fila['descripcion'].strip(),
        'precio': precio,
        'stock': stock,
        'imagen': ruta_imagen,
    }
