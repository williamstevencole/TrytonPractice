from trytond.model import ModelSQL, ModelView, fields

class MiModelo(ModelSQL, ModelView):
    """Ejemplo de modelo"""
    __name__ = 'mi_modulo.mi_modelo'

    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')