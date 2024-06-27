import re

# Función para generar variaciones de una palabra en número y género
def generar_variaciones(palabra):
    variaciones = [palabra]
    # Si la palabra termina en 'o', generar variaciones en 'a', 'os' y 'as'
    if palabra.endswith('o'):
        variaciones.append(palabra[:-1] + 'a')
        variaciones.append(palabra + 's')
        variaciones.append(palabra[:-1] + 'as')
    # Si la palabra termina en 'a', generar variaciones en 'o', 'as' y 'os'
    elif palabra.endswith('a'):
        variaciones.append(palabra[:-1] + 'o')
        variaciones.append(palabra + 's')
        variaciones.append(palabra[:-1] + 'os')
    # Si la palabra termina en 'e', generar variación en 'es'
    elif palabra.endswith('e'):
        variaciones.append(palabra + 's')
    # Si la palabra termina en 'l', 'n' o 'r', generar variación en 'es'
    elif palabra.endswith('l') or palabra.endswith('n') or palabra.endswith('r'):
        variaciones.append(palabra + 'es')
    # Para otros casos, generar variación en 's'
    else:
        variaciones.append(palabra + 's')
    return variaciones

# Función para generar listas de variaciones a partir de una lista de palabras
def generar_listas_variaciones(lista_palabras):
    lista_variaciones = []
    # Para cada palabra en la lista, generar sus variaciones y añadirlas a la lista de variaciones
    for palabra in lista_palabras:
        lista_variaciones.extend(generar_variaciones(palabra))
    return list(set(lista_variaciones))  # Eliminar duplicados

# Listas de palabras positivas, negativas y neutras (sin acentos y en minúsculas)
# Las palabras son pasadas a la función generar_listas_variaciones para incluir sus variaciones en número y género
palabras_positivas = generar_listas_variaciones([
    'gracias', 'por favor', 'ayuda', 'resolver', 'excelente', 'bueno', 'bien', 'fantastico', 'perfecto',
    'genial', 'asombroso', 'maravilloso', 'esplendido', 'magnifico', 'grandioso', 'estupendo', 'increible',
    'extraordinario', 'positivo', 'satisfactorio', 'brillante', 'fenomenal', 'impresionante', 'eficaz', 'eficiente',
    'rapido', 'puntual', 'comodo', 'seguro', 'fiable', 'amable', 'cortes', 'educado', 'respetuoso', 'simpatico',
    'agradable', 'cordial', 'dispuesto', 'atento', 'considerado', 'profesional', 'diligente', 'responsable',
    'competente', 'excepcional', 'impecable', 'meticuloso', 'cuidadoso', 'detallista', 'minucioso', 'preciso',
    'justo', 'equilibrado', 'coherente', 'logico', 'razonable', 'sensato', 'inteligente', 'listo', 'ingenioso',
    'habil', 'talentoso', 'virtuoso', 'artistico', 'creativo', 'innovador', 'original', 'visionario', 'perceptivo',
    'perspicaz', 'sagaz', 'agudo', 'brillante', 'lucido', 'sabio', 'experto', 'maestro', 'veterano', 'guia',
    'lider', 'jefe', 'mentor', 'entrenador', 'tutor', 'profesor', 'docente', 'facilitador', 'orador', 'disertante',
    'conferenciante', 'comunicador', 'informador', 'notificador', 'anunciador', 'publicista', 'promotor', 'difusor',
    'divulgador', 'recomendador', 'consultor', 'asesor', 'consejero', 'guia', 'psicologo', 'terapeuta', 'orientador'
])

palabras_negativas = generar_listas_variaciones([
    'mal', 'desastre', 'harto', 'cansado', 'cancelar', 'malo', 'deficiente', 'terrible', 
    'pesimo', 'inaceptable', 'horrible', 'decepcionante', 'incompetente', 'frustrante', 'insatisfactorio', 
    'lento', 'tardado', 'dificil', 'imposible', 'queja', 'reclamo', 'denuncia', 'fallo', 'error', 
    'defecto', 'defectuoso', 'incidente', 'inconveniente', 'irresuelto', 'insuficiente', 'fallido', 
    'engorroso', 'problematico', 'lamentable', 'aburrido', 'molesto', 'enojado', 'furioso', 'enfurecido',
    'indignado', 'agrio', 'amargo', 'desagradable', 'desesperante', 'triste', 'deprimente', 'abrumador',
    'deprimido', 'abatido', 'agobiado', 'perturbador', 'desmoralizador', 'desalentador', 'intolerable',
    'insoportable', 'irritante', 'irrespetuoso', 'arrogante', 'prepotente', 'soberbio', 'altanero',
    'despectivo', 'desdeñoso', 'cinico', 'sarcasmo', 'insulto', 'humillante', 'ofensivo', 'degradante',
    'hostil', 'antipatico', 'desalmado', 'cruel', 'brutal', 'sadico', 'malvado', 'vil', 'corrupto', 'deshonesto',
    'mentiroso', 'falso', 'enganador', 'tramposo', 'ladrones', 'timador', 'estafador', 'defraudador',
    'delincuente', 'criminal', 'inmoral', 'perverso', 'pecador', 'malevolo', 'demoniaco', 'siniestro',
    'oscuro', 'tenebroso', 'maldito', 'diabolico'
])

palabras_neutras = generar_listas_variaciones([
    'problema', 'inconveniente', 'dificultad', 'complicacion', 'retraso', 'espera', 'demora', 'consulta',
    'solicitud', 'peticion', 'pregunta', 'duda', 'incertidumbre', 'confusion', 'indecision', 'cuestion', 
    'tramite', 'procedimiento', 'proceso', 'operacion', 'situacion', 'caso', 'circunstancia', 'condicion'
])

# Crear patrones de expresiones regulares a partir de las listas (sin acentos y en minúsculas)
# Estos patrones permiten buscar las palabras en los textos
saludos_bienvenida = re.compile(r'\bbuen(?:os?)? (?:dias?|tardes?|noches?)\b', re.IGNORECASE)
despedidas = re.compile(r'\b(?:hasta luego|adios|que tenga un buen dia|que tenga un lindo resto de jornada|que le vaya bien|que tenga una buena tarde|que tenga una buena noche|nos vemos|hasta la proxima|cuidese|buenas noches)\b', re.IGNORECASE)
identificacion = re.compile(r'\b(?:documento|cedula)\b', re.IGNORECASE)
expresiones_positivas = re.compile(r'\b(?:' + '|'.join(palabras_positivas) + r')\b', re.IGNORECASE)
expresiones_negativas = re.compile(r'\b(?:' + '|'.join(palabras_negativas) + r')\b', re.IGNORECASE)
expresiones_neutras = re.compile(r'\b(?:' + '|'.join(palabras_neutras) + r')\b', re.IGNORECASE)
preguntas_ayuda = re.compile(r'\b(?:algo mas|otra (?:cosa|pregunta|inquietud|duda|consulta|ayuda)|que mas|alguna otra (?:pregunta|inquietud|consulta|cosa|duda|ayuda|necesidad|problema|asunto|detalle))\b', re.IGNORECASE)

# Función para preprocesar el texto
def preprocesar_texto(texto):
    # Convertir a minúsculas
    texto = texto.lower()
    # Eliminar acentos
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u'
    }
    for acento, letra in acentos.items():
        texto = texto.replace(acento, letra)
    return texto

# Función para procesar el texto del funcionario
def evaluar_funcionario(texto):
    # Preprocesar el texto para convertirlo a minúsculas y eliminar acentos
    texto = preprocesar_texto(texto)
    puntuacion = 0
    detalles = []

    # Buscar saludos de bienvenida
    if saludos_bienvenida.search(texto):
        puntuacion += 1
        detalles.append("Saludo de bienvenida detectado")
    else:
        detalles.append("Falta saludo de bienvenida")

    # Buscar despedidas
    if despedidas.search(texto):
        puntuacion += 1
        detalles.append("Despedida detectada")
    else:
        detalles.append("Falta despedida")

    # Buscar solicitudes de identificación
    if identificacion.search(texto):
        puntuacion += 1
        detalles.append("Solicitud de identificacion detectada")
    else:
        detalles.append("Falta solicitud de identificacion")

    # Buscar expresiones positivas
    if expresiones_positivas.search(texto):
        puntuacion += 1
        detalles.append("Uso de expresiones positivas detectado")
    else:
        detalles.append("Falta uso de expresiones positivas")

    # Buscar preguntas de ayuda adicional
    if preguntas_ayuda.search(texto):
        puntuacion += 1
        detalles.append("Pregunta de ayuda adicional detectada")
    else:
        detalles.append("Falta pregunta de ayuda adicional")

    # Ajustar la puntuacion a una escala del 1 al 5
    puntuacion = max(1, min(puntuacion, 5))

    return puntuacion, detalles

# Función para procesar el texto del cliente
def evaluar_cliente(texto):
    # Preprocesar el texto para convertirlo a minúsculas y eliminar acentos
    texto = preprocesar_texto(texto)
    puntuacion = 5  # Empezamos con una puntuacion base de 5
    palabras_buenas = []
    palabras_malas = []
    palabras_neutras_encontradas = []

    # Buscar y almacenar palabras positivas
    buenas = expresiones_positivas.findall(texto)
    palabras_buenas.extend(buenas)

    # Buscar y almacenar palabras negativas
    malas = expresiones_negativas.findall(texto)
    palabras_malas.extend(malas)

    # Buscar y almacenar palabras neutras
    neutras = expresiones_neutras.findall(texto)
    palabras_neutras_encontradas.extend(neutras)

    # Ajustar la puntuacion en base a las palabras encontradas
    puntuacion += len(buenas)
    puntuacion -= len(malas)

    # Ajustar la puntuacion a una escala del 1 al 5
    puntuacion = max(1, min(puntuacion, 5))

    return puntuacion, palabras_buenas, palabras_malas, palabras_neutras_encontradas

# Función para calificar la experiencia en base a la puntuación
def calificar_experiencia(puntuacion):
    if puntuacion > 3:
        return "positiva"
    elif puntuacion == 3:
        return "neutra"
    else:
        return "negativa"

# Función para preguntar al usuario si desea incluir una palabra neutra como negativa
def preguntar_incluir_palabra_neutra(palabra):
    respuesta = input(f"¿Desea incluir la palabra '{palabra}' como negativa? (si/no): ").strip().lower()
    return respuesta == 'si'

# Función principal para evaluar ambos archivos
def evaluar_llamada(archivo_funcionario, archivo_cliente):
    with open(archivo_funcionario, 'r', encoding='utf-8') as f_funcionario:
        texto_funcionario = f_funcionario.read()

    with open(archivo_cliente, 'r', encoding='utf-8') as f_cliente:
        texto_cliente = f_cliente.read()

    print("Evaluando el texto del funcionario...")
    puntuacion_funcionario, detalles_funcionario = evaluar_funcionario(texto_funcionario)
    calificacion_funcionario = calificar_experiencia(puntuacion_funcionario)
    print(f"Puntuacion del funcionario: {puntuacion_funcionario} (Experiencia {calificacion_funcionario})")
    for detalle in detalles_funcionario:
        print(f" - {detalle}")

    print("\nEvaluando el texto del cliente...")
    puntuacion_cliente, palabras_buenas, palabras_malas, palabras_neutras = evaluar_cliente(texto_cliente)
    calificacion_cliente = calificar_experiencia(puntuacion_cliente)
    print(f"Puntuacion del cliente: {puntuacion_cliente} (Experiencia {calificacion_cliente})")
    print(f"Palabras buenas detectadas: {', '.join(palabras_buenas) if palabras_buenas else 'Ninguna'}")
    print(f"Palabras malas detectadas: {', '.join(palabras_malas) if palabras_malas else 'Ninguna'}")
    print(f"Palabras neutras detectadas: {', '.join(palabras_neutras) if palabras_neutras else 'Ninguna'}")

    # Inicializar la longitud original de palabras negativas
    longitud_original_negativas = len(palabras_negativas)

    # Preguntar al usuario si desea incluir palabras neutras como negativas
    for palabra in palabras_neutras:
        if preguntar_incluir_palabra_neutra(palabra):
            palabras_negativas.append(palabra)

    # Recalcular la puntuacion del cliente si se añadieron palabras neutras a negativas
    if len(palabras_negativas) > longitud_original_negativas:
        # Actualizar expresiones_negativas
        global expresiones_negativas
        expresiones_negativas = re.compile(r'\b(?:' + '|'.join(palabras_negativas) + r')\b', re.IGNORECASE)
        puntuacion_cliente, palabras_buenas, palabras_malas, _ = evaluar_cliente(texto_cliente)
        calificacion_cliente = calificar_experiencia(puntuacion_cliente)
        print(f"\nNueva Puntuacion del cliente: {puntuacion_cliente} (Experiencia {calificacion_cliente})")
        print(f"Palabras malas detectadas (incluyendo las nuevas): {', '.join(palabras_malas) if palabras_malas else 'Ninguna'}")

# Ejemplo de uso
archivo_funcionario = 'funcionario.txt'
archivo_cliente = 'cliente.txt'

evaluar_llamada(archivo_funcionario, archivo_cliente)
