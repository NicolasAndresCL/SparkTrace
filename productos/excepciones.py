class APIError(Exception):
    """Error al comunicarse con la API externa."""
    def __init__(self, mensaje, status_code=None):
        self.mensaje = mensaje
        self.status_code = status_code
        super().__init__(f"{mensaje} (status: {status_code})")
