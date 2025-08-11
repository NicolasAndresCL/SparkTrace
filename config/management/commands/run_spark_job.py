from django.core.management.base import BaseCommand
from spark_jobs.process_products import run_job
from auditlog.utils import log_event

class Command(BaseCommand):
    help = "Lanza job PySpark para procesar productos"

    def handle(self, *args, **kwargs):
        result = run_job("data/products.csv")
        log_event("spark_job_executed", payload=result)
        self.stdout.write(self.style.SUCCESS("Job ejecutado con éxito"))
