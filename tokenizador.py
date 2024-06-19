import re

class AFD:
    def __init__(self, patrones):
        self.patrones = patrones

    def procesar_texto(self, texto):
        tokens = []
        puntuacion = 0
        
        # Dividir el texto en palabras
        palabras = texto.split()
        
        for palabra in palabras:
            print(f"Procesando palabra: {palabra}")
            matched = False
            for patron, token, valor in self.patrones:
                if re.fullmatch(patron, palabra):
                    tokens.append(token)
                    puntuacion += valor
                    matched = True
                    print(f"  Coincide con patrón: {patron}")
                    print(f"  Token asignado: {token}, Valor: {valor}")
                    break
            if not matched:
                print(f"  No se encontró ningún patrón para la palabra: {palabra}")
        
        return tokens, puntuacion

# Definir patrones, tokens y valores de puntuación
patrones = [
    (r'buen[oa]s? (d[ií]as?|tardes?|noches?)', 'ATC_BUENA', 1),
    (r'hasta luego', 'ATC_BUENA', 1),
    (r'documento', 'ATC_NEUTRA', 0),
    (r'c[eé]dula', 'ATC_NEUTRA', 0),
    (r'gracias', 'EXP_BUENA', 1),
    (r'por favor', 'EXP_BUENA', 1),
    (r'mal[oa]?s?', 'EXP_MALA', -1),
    (r'desastre', 'EXP_MALA', -1),
    (r'hart[oa]?s?', 'EXP_MALA', -1),
    (r'cansad[oa]?s?', 'EXP_MALA', -1),
    (r'cancelar', 'EXP_MALA', -1)
]

# Crear una instancia del AFD con los patrones
afd = AFD(patrones)

# Función para leer un archivo y devolver su contenido en minúsculas
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read().lower()

# Función principal
def main():
    # Leer archivos de entrada
    interaccion_funcionario = leer_archivo('funcionario.txt')
    interaccion_cliente = leer_archivo('cliente.txt')

    # Evaluar interacciones con el AFD
    print("\nEvaluando interacción del funcionario...")
    tokens_funcionario, puntuacion_funcionario = afd.procesar_texto(interaccion_funcionario)
    print("\nEvaluando interacción del cliente...")
    tokens_cliente, puntuacion_cliente = afd.procesar_texto(interaccion_cliente)

    # Mostrar resultados
    print("\nResultados:")
    print("Tokens funcionario:", tokens_funcionario)
    print("Puntuación funcionario:", puntuacion_funcionario)
    print("Tokens cliente:", tokens_cliente)
    print("Puntuación cliente:", puntuacion_cliente)

    # Calificación final
    calificacion_funcionario = "Desempeño del funcionario: " + ("Bueno" if puntuacion_funcionario > 0 else "Malo")
    calificacion_cliente = "Experiencia del cliente: " + ("Buena" if puntuacion_cliente > 0 else "Mala")

    print(calificacion_funcionario)
    print(calificacion_cliente)

if __name__ == "__main__":
    main()
