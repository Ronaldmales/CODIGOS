import math

def solve_quadratic_equation(a, b, c):
    # Calcula el discriminante
    discriminant = b**2 - 4*a*c
    
    # Comprueba si la ecuación tiene soluciones reales
    if discriminant < 0:
        return "La ecuación no tiene soluciones reales."
    elif discriminant == 0:
        # Si el discriminante es cero, hay una solución real
        x = -b / (2*a)
        return f"La solución única es x = {x}"
    else:
        # Si el discriminante es positivo, hay dos soluciones reales
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Las soluciones son x1 = {x1} y x2 = {x2}"

# Ejemplo de uso
coeficiente_a = float(input("Introduce el coeficiente a: "))
coeficiente_b = float(input("Introduce el coeficiente b: "))
coeficiente_c = float(input("Introduce el coeficiente c: "))

soluciones = solve_quadratic_equation(coeficiente_a, coeficiente_b, coeficiente_c)
print(soluciones)
