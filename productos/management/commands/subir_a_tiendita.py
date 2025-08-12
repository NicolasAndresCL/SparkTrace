from django.core.management.base import BaseCommand
from productos.utils.csv_loader import cargar_productos_desde_csv
from productos.services.tiendita_api import enviar_producto
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Carga productos desde CSV y los envía a Tiendita de Marian"

    def add_arguments(self, parser):
        parser.add_argument('--archivo', type=str, required=True, help='Ruta al archivo CSV')

    def handle(self, *args, **options):
        ruta_csv = options['archivo']
        productos = cargar_productos_desde_csv(ruta_csv)

        for producto in productos:
            try:
                respuesta = enviar_producto(producto)
                logger.info(f"✅ Producto enviado: {producto['nombre']} → {respuesta.status_code}")
            except Exception as e:
                logger.warning(f"❌ Error al enviar {producto['nombre']}: {str(e)}")
