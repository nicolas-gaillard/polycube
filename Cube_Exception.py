""" Classe permettant de lever des exceptions lorsque le cube est mal formé

    :param Exception: message informatif expliquant la cause de la levée de l'exception
"""
class Cube_Exception(Exception):
    def __init__(self,raison):
        self.raison = raison
    
    def __str__(self):
        return self.raison