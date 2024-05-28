class Alumno:
    def __init__(self, curp, codmunicipio, nombre_s_alum, paternoalum, maternoalum, nivelcursa):
        self.curp = curp
        self.codmunicipio = codmunicipio
        self.nombre_s_alum = nombre_s_alum
        self.paternoalum = paternoalum
        self.maternoalum = maternoalum
        self.nivelcursa = nivelcursa
    
    def __repr__(self):
        return f"Alumno(CURP={self.curp}, CODMUNICIPIO={self.codmunicipio}, NOMBRE_S_ALUM={self.nombre_s_alum}, PATERNOALUM={self.paternoalum}, MATERNOALUM={self.maternoalum}, NIVELCURSA={self.nivelcursa})"
