class Municipio:
    def __init__(self, codmunicipio, nombremunicipio):
        self.codmunicipio = codmunicipio
        self.nombremunicipio = nombremunicipio

    def __repr__(self):
        return f"Municipio(CODMUNICIPIO={self.codmunicipio}, NOMBREMUNICIPIO={self.nombremunicipio})"
