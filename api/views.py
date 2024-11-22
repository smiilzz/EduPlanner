from django.shortcuts import render
from .models import Api
from django.http import JsonResponse
import requests

def Lista_Api(request):
    fechas = Api.objects.all()
    return render(request, 'api/Lista_Api.html', {'fechas': fechas})

def obtener_feriados(request):
    url = "https://apis.digital.gob.cl/fl/feriados/2024"  # URL de la API de terceros

    try:
        # Realizar la solicitud GET a la API
        respuesta = requests.get(url)

        # Verificar si la solicitud fue exitosa (código 200)
        if respuesta.status_code == 200:
            feriados = respuesta.json()  # Convertir la respuesta a JSON
            return JsonResponse(feriados, safe=False)  # Retornar la respuesta como JSON
        else:
            # En caso de error, manejar el estado
            return JsonResponse({'error': 'No se pudo obtener la información de feriados.'}, status=respuesta.status_code)

    except Exception as e:
        # Manejar cualquier error de conexión u otro tipo de error
        return JsonResponse({'error': str(e)}, status=500)


def lista_proyectos_y_feriados(request):
    # Obtener datos de tu modelo
    fechas= list(Api.objects.values())  # Convertir QuerySet a lista

    # Obtener los feriados desde la API de terceros
    url = "https://apis.digital.gob.cl/fl/feriados/2024"
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            feriados = respuesta.json()
        else:
            fechas = []
    except Exception as e:
        feriados = []  # En caso de error, feriados estará vacío

    # Combinar los datos de proyectos y feriados
    data = {
        'fechas': fechas,
        'feriados': feriados,
    }

    return JsonResponse(data, safe=False)  # Retornar ambos como JSON'''

def proyectos_y_feriados_html(request):
    # Obtener los datos de tu modelo
    fechas = Api.objects.all()

    # Obtener los feriados desde la API externa
    url = "https://apis.digital.gob.cl/fl/feriados/2024"
    try:
        respuesta = requests.get(url)
        print(f"Estado de la respuesta: {respuesta.status_code}")  # Imprime el código de estado
        print(f"Respuesta JSON: {respuesta.text}")  # Imprime el cuerpo de la respuesta

        if respuesta.status_code == 200:
            feriados = respuesta.json()  # Convierte la respuesta en JSON
            feriados = feriados.get('data', [])  # Accede a la clave 'data' que contiene los feriados
        else:
            feriados = []
    except Exception as e:
        feriados = []  # Si hay un error, los feriados estarán vacíos
        print(f"Error al realizar la solicitud: {e}")  # Imprime el error

    # Pasar los datos de fechas y feriados al template
    contexto = {
        'fechas': fechas,
        'feriados': feriados,
    }
    return render(request, 'api/proyectos_y_feriados.html', contexto)