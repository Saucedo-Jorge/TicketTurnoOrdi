class DetalleCita:
    def __init__(self, idcita, curp, numturno, asuntotratar):
        self.idcita = idcita
        self.curp = curp
        self.numturno = numturno
        self.asuntotratar = asuntotratar
        
    
    def __repr__(self):
        return f"DetalleCita(IdCita={self.idcita}, CURP={self.curp}, NumTurno={self.numturno}, AsuntoTratar={self.asuntotratar})"
