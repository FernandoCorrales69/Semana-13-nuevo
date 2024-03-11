def calcular_temperatura_promedio(datos_temperaturas):
    # Inicializamos un diccionario para almacenar las temperaturas promedio de cada ciudad
    temperatura_promedio_por_ciudad = {}

    # Recorremos los datos de temperaturas
    for ciudad, temperaturas_por_semana in datos_temperaturas.items():
        # Inicializamos una lista para almacenar las temperaturas promedio por semana
        temperaturas_promedio_por_semana = []

        # Recorremos las temperaturas por semana
        for semana, temperaturas in temperaturas_por_semana.items():
            # Calculamos la temperatura promedio de la semana
            temperatura_promedio_semana = sum(temperaturas) / len(temperaturas)
            # Agregamos la temperatura promedio de la semana a la lista
            temperaturas_promedio_por_semana.append(temperatura_promedio_semana)

        # Calculamos la temperatura promedio de la ciudad
        temperatura_promedio_ciudad = sum(temperaturas_promedio_por_semana) / len(temperaturas_promedio_por_semana)
        # Almacenamos la temperatura promedio de la ciudad en el diccionario
        temperatura_promedio_por_ciudad[ciudad] = temperatura_promedio_ciudad

    return temperatura_promedio_por_ciudad


# Ejemplo de datos de temperaturas
datos_temperaturas = {
    'Quito': {
        'Semana 1': [20, 22, 21, 23, 25],
        'Semana 2': [22, 23, 24, 21, 20]
    },
    'Latacunga': {
        'Semana 1': [18, 19, 20, 22, 21],
        'Semana 2': [17, 18, 20, 19, 21]
    }
}

# Llamamos a la función y mostramos los resultados
temperatura_promedio_por_ciudad = calcular_temperatura_promedio(datos_temperaturas)
for ciudad, temperatura_promedio in temperatura_promedio_por_ciudad.items():
    print(f'Temperatura promedio en {ciudad}: {temperatura_promedio}')


