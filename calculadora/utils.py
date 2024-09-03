def calcular_consumo(data):
    return (data['consumo_actual'] - data['consumo_anterior']) * data['precio_kwh']