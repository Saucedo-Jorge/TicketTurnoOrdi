from models.entities.Cita import Cita
from models.entities.Alumno import Alumno
from models.entities.Municipio import Municipio
from models.entities.DetalleCita import DetalleCita

class EntityFactory:
    @staticmethod
    def create_entity(entity_type, *args, **kwargs):
        if entity_type == 'cita':
            return Cita(*args, **kwargs)
        elif entity_type == 'alumno':
            return Alumno(*args, **kwargs)
        elif entity_type == 'municipio':
            return Municipio(*args, **kwargs)
        elif entity_type == 'detallecita':
            return DetalleCita(*args, **kwargs)
        else:
            raise ValueError(f"Unknown entity type: {entity_type}")
