# Datos personales
nombre = "Juan Pérez"
direccion = "Calle Principal 123, Ciudad"
telefono = "1234567890"
correo = "juan.perez@example.com"

# Experiencia laboral
experiencia1_empresa = "Empresa ABC"
experiencia1_puesto = "Desarrollador de software"
experiencia1_fecha = "2018 - 2021"
experiencia1_responsabilidades = "- Desarrollo y mantenimiento de aplicaciones web\n- Colaboración en proyectos en equipo"

# Educación
educacion_titulo = "Licenciatura en Ingeniería de Software"
educacion_institucion = "Universidad XYZ"
educacion_fecha = "2014 - 2018"

# Habilidades
habilidades = ["Python", "Java", "HTML/CSS", "JavaScript", "Bases de datos", "Resolución de problemas"]

# Imprimir hoja de vida
print("HOJA DE VIDA")
print("------------")
print("Nombre: ", nombre)
print("Dirección: ", direccion)
print("Teléfono: ", telefono)
print("Correo electrónico: ", correo)
print("\nExperiencia laboral:")
print(experiencia1_fecha, "-", experiencia1_empresa)
print("Puesto: ", experiencia1_puesto)
print("Responsabilidades:\n", experiencia1_responsabilidades)
print("\nEducación:")
print(educacion_fecha, "-", educacion_titulo)
print("Institución: ", educacion_institucion)
print("\nHabilidades:")
for habilidad in habilidades:
    print("-", habilidad)
