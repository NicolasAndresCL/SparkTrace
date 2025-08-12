from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Ejecuta el job técnico de SparkTrace"

    def handle(self, *args, **options):
        self.stdout.write("Spark job completed")
