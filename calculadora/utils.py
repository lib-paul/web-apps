def calcular_consumo(data):
    return (data['consumo_anterior'] - data['consumo_actual']) * data['precio_kwh']