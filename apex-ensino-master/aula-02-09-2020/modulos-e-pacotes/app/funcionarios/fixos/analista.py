from .. import mostrar_info


class Analista:
    def __init__(self):
        self.cargo = "Analista"
        self.setor = "TI"

    def info(self):
        return mostrar_info(self.cargo, self.setor)
