import functools

def __pitagoras_validations(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        __num_validations(*args, **kwargs)
        __calc_validation(*args, **kwargs)

        return func(*args, **kwargs)
    
    return wrapper

def __num_validations(*args, **kwargs):
    a = kwargs.get('a', args[0] if args else None)
    b = kwargs.get('b', args[1] if len(args) > 1 else None)

    variables_verification = (isinstance(a, (int, float)) and isinstance(b, (int, float)))
    msg = 'Definir um valor numérico para as variáveis "a" e "b"'
    assert variables_verification, msg

def __calc_validation(*args, **kwargs):
    calc = kwargs.get('calc', args[2] if len(args) > 2 else 'hip')

    calc_verification = (calc in ('hip', 'cat'))
    msg = f"Valor '{calc}' para parâmetro Calc não é válido.\nOs valores possíveis para o parâmetro Calc são: 'hip' (para cálculo da hipotenusa) e 'cat' (para cálculo do cateto)."
    assert calc_verification, msg


