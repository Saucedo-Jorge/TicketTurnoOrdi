class Cita:
    def __init__(self, idcita, quienr, telefonoqr, correoqr, status):
        self.idcita = idcita
        self.quienr = quienr
        self.telefonoqr = telefonoqr
        self.correoqr = correoqr
        self.status = status

    def __repr__(self):
        return f"Cita(IDCITA={self.idcita}, QUIENR={self.quienr}, TELEFONOQR={self.telefonoqr}, CORREOQR={self.correoqr}, STATUS={self.status})"
