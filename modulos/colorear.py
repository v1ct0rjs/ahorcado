
class MyException(Exception):                                                   # Clase padre de las excepciones
    def __init__(self,mensaje_err: str) -> None:                                # Constructor de la clase
        super().__init__(f'Error: {mensaje_err}')                               # Llamamos al constructor de la clase padre

class ColorInexistente(MyException):                                            # Clase hija de MyException
    def __init__(self, mensaje_err: str) -> None:                               # Constructor de la clase
        super().__init__(mensaje_err)                                           # Llamamos al constructor de la clase padre

class FormatoInvalido(MyException):                                             # Clase hija de MyException
    def __init__(self, mensaje_err: str) -> None:                               # Constructor de la clase
        super().__init__(mensaje_err)                                           # Llamamos al constructor de la clase padre




def printcolor(color, texto, *formatos):
    """Imprime el texto con el color y los formatos especificados."""
    try:
        colores = {                                                              # Diccionario con los códigos de colores                     
            'rojo': '\033[91m',
            'verde': '\033[92m',
            'amarillo': '\033[93m',
            'azul': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'blanco': '\033[97m'
        }
        
        if color not in colores:                                                  # Si el color no está en el diccionario                
            raise ColorInexistente(f"El color '{color}' no existe.")              # Lanzamos una excepción
        
        formatos_validos = {'negrita', 'subrayado', 'invertido', 'difuminado', 'tachado', 'parpadeo', 'normal'} # Conjunto con los formatos válidos
        for formato in formatos:
            if formato.lower() not in formatos_validos:                             # Si el formato no está en el conjunto
                raise FormatoInvalido(f"El formato '{formato}' no es válido.")      # Lanzamos una excepción
        
        codigo_formato = ''
        for formato in formatos:                                                   # Recorremos los formatos
            if formato.lower() == 'negrita':
                codigo_formato += '\033[1m'
            elif formato.lower() == 'subrayado':
                codigo_formato += '\033[4m'
            elif formato.lower() == 'invertido':
                codigo_formato += '\033[7m'
            elif formato.lower() == 'difuminado':
                codigo_formato += '\033[2m'
            elif formato.lower() == 'tachado':
                codigo_formato += '\033[9m'
            elif formato.lower() == 'parpadeo':
                codigo_formato += '\033[5m'
            elif formato.lower() == 'normal':
                codigo_formato += '\033[0m'
        
        print(f"{codigo_formato}{colores[color]}{texto}\033[0m")              # Imprimimos el texto con el color y los formatos
    
    except (ColorInexistente, FormatoInvalido) as e:                          # Capturamos las excepciones
        print(e)                                                              # Imprimimos el mensaje de error        
        
 