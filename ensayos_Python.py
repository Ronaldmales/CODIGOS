def create_essay(title, introduction, body, conclusion):
    essay = f"Titulo: {title}\n\n"
    essay += "Introducción:\n"
    essay += f"{introduction}\n\n"
    essay += "Cuerpo del ensayo:\n"
    essay += f"{body}\n\n"
    essay += "Conclusión:\n"
    essay += f"{conclusion}"
    
    return essay

# Ejemplo de uso
essay_title = input("Ingrese el título del ensayo: ")
essay_introduction = input("Ingrese la introducción del ensayo: ")
essay_body = input("Ingrese el cuerpo del ensayo: ")
essay_conclusion = input("Ingrese la conclusión del ensayo: ")

ensayo = create_essay(essay_title, essay_introduction, essay_body, essay_conclusion)
print(ensayo)
