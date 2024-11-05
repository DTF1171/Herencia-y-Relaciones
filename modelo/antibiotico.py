from .producto import _Producto

class _Antibiotico(_Producto):
    def __init__(self, registro_ICA, nombre, valor, dosis, tipo_animal):
        super().__init__(registro_ICA, nombre, valor)
        dosis = int(dosis)
        if dosis < 400 or dosis > 600:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg.")
        if tipo_animal not in ["Bovino", "Caprino", "Porcino"]:
            raise ValueError("El tipo de animal debe ser Bovino, Caprino o Porcino.")
        self.__dosis = dosis
        self.__tipo_animal = tipo_animal

    # Getters
    def get_dosis(self):
        return self.__dosis

    def get_tipo_animal(self):
        return self.__tipo_animal

    # Setters
    def set_dosis(self, dosis):
        if dosis < 400 or dosis > 600:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg.")
        self.__dosis = dosis

    def set_tipo_animal(self, tipo_animal):
        if tipo_animal not in ["Bovino", "Caprino", "Porcino"]:
            raise ValueError("El tipo de animal debe ser Bovino, Caprino o Porcino.")
        self.__tipo_animal = tipo_animal

    def __str__(self):
        return f"Antibiótico {self.get_nombre()} - ${self.get_valor()} - Dosis: {self.__dosis}Kg - Tipo: {self.__tipo_animal}"
