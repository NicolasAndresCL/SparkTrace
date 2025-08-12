import pytest
from io import StringIO
from django.core.management import call_command, get_commands
from django.core.management.base import CommandError

def test_comando_run_spark_job_registrado():
    """
    Verifica que el comando 'run_spark_job' esté registrado en Django.
    """
    comandos = get_commands()
    assert "run_spark_job" in comandos

def test_run_spark_job_ejecucion_exitosa():
    """
    Ejecuta el comando y valida que no arroje errores.
    """
    out = StringIO()
    try:
        call_command("run_spark_job", stdout=out)
    except CommandError as e:
        pytest.fail(f"Comando no reconocido: {e}")
    except Exception as e:
        pytest.fail(f"Error al ejecutar el comando: {e}")

    salida = out.getvalue()
    assert "Spark job completed" in salida or "Job ejecutado" in salida
