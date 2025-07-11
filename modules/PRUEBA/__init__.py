from trytond.pool import Pool

__all__ = ['register']


def register():
    Pool.register(
        module='PRUEBA', type_='model')
    Pool.register(
        module='PRUEBA', type_='wizard')
    Pool.register(
        module='PRUEBA', type_='report')
