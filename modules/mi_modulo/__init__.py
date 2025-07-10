from trytond.pool import Pool
from .models.mi_modulo import MiModelo

def register():
    Pool.register(
        MiModelo,
        module='mi_modulo', type_='model'
    )
