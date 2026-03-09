from odoo import models, fields


class HardwareItem(models.Model):
    _name = "hardware.item"
    _description = "Equipos de hardware"

    name = fields.Char(string="Nombre del equipo", required=True)
    tipo = fields.Selection(
        [
            ("server", "Servidor"),
            ("laptop", "Portátil"),
            ("desktop", "Escritorio"),
            ("printer", "Impresora"),
            ("switch", "Switch"),
            ("nas", "Almacenamiento NAS"),
            ("other", "Otro"),
        ],
        string="Tipo de dispositivo",
        required=True,
    )
    ip_address = fields.Char(string="Dirección IP")
    notas = fields.Text(string="Observaciones")
