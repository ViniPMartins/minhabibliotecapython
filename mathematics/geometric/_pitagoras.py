import numpy as np
from ..utils import __pitagoras_validations

@__pitagoras_validations
def Pitagoras(a, b, calc='hip') -> float:
    #Docstrings
    '''
    Esta função tem como objetivo automatizar o cálculo de pitagoras, 
    onde tentamos achar o valor de um dos lados de um triângulo retângulo.

    Parametros:
    -----------
    * ``a`` = int or float
        Valor conhecido de um dos lados do triângulo retângulo, 
        podendo ser um cateto ou a hiponetusa.
    * ``b`` = int or float
        Valor conhecido do segundo lado do triângulo retângulo,
        podendo ser um cateto ou a hiponetusa.
    * ``calc`` = 'hip', 'cat', default='hip'
        Valor que deseja encontrar sendo:
            - hip = hipotenusa
            - cat = cateto
    '''

    if calc == 'hip':
        c = np.sqrt((a**2) + (b**2))
    elif calc == 'cat':
        c = np.sqrt((max(a, b)**2) - (min(a, b)**2))

    return c