from django.core.exceptions import ValidationError

def validar_par(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s no es un numero par',
            params={'value': value}
        )

def validar_nombre_categoria(value):
    if value == 'No permitido':
        raise ValidationError("No es una opcion permitida")

def validar_nombre_subject(value):
    if value == 'Comida':
        raise ValidationError("No es una opcion permitida")
