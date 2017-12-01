import re

def esFechaValida(fecha):
    expresionRegularFecha = "[0-3]{1}[0-9]{1}\/[0-1]{1}[0-9]{1}\/[0-9]{4}"
    if re.match(expresionRegularFecha, fecha):
        return True
    else:
        return False
