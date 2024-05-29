class NumTurno:
    def __init__(self, nombremuni, numcita):
        self.nombremuni = nombremuni
        self.numcita = numcita
        
    
    def __repr__(self):
        return f"DetalleCita(IdCita={self.idcita}, CURP={self.curp}, NumTurno={self.numturno}, AsuntoTratar={self.asuntotratar})"
