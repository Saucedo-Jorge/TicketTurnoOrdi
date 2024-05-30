class DetalleCita:
    def __init__(self, idcita, curp, numturno, asuntotratar):
        self.idcita = idcita
        self.curp = curp
        self.numturno = numturno
        self.asuntotratar = asuntotratar
        
    
    def __repr__(self):
        return f"DetalleCita(idcita={self.idcita}, curp={self.curp}, numturno={self.numturno}, asuntotratar={self.asuntotratar})"
