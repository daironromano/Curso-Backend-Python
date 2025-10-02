from abc import ABC , abstractmethod
from math import pi

class FormaGeometrica(ABC):

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return pi * self.raio ** 2

    def calcularPerimetro(self):
        return 2 * pi * self.raio
    
class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

def gerarRelatorio(formas):
    print('RELATÓRIO FORMAS GEOMÉTRICAS')
    for i, forma in enumerate(formas):
        area = forma.cacularArea()
        perimetro = forma.calcularPerimetro()
        print(forma)
        print(f'Área: {area}\n Perimetro: {perimetro}')
        
    area_total = sum(forma.cacularArea for forma in formas)
    perimetro_total = sum(forma.calcularPerimetro for forma in formas)
    print(area_total, perimetro_total)

r = Retangulo(10, 20)
print(r.calcularArea())