from productos.utils.csv_loader import cargar_productos_desde_csv
from productos.services.tiendita_api import enviar_producto
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = 'Carga productos desde CSV y los envía a Tiendita'

    def add_arguments(self, parser):
        parser.add_argument('ruta_csv', type=str)

    def handle(self, *args, **options):
        ruta_csv = options['ruta_csv']
        productos = cargar_productos_desde_csv(ruta_csv)

        for producto in productos:
            try:
                resultado = enviar_producto(producto)
                self.stdout.write(self.style.SUCCESS(f"Producto enviado: {resultado['id']}"))
            except ValidationError as e:
                self.stdout.write(self.style.ERROR(f"Error: {e}"))
