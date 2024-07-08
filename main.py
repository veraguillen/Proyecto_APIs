
from fastapi import FastAPI, HTTPException, Query
import pandas as pd

# Crear una instancia de FastAPI
app = FastAPI()



# Función para cargar datos desde un archivo CSV
def cargar_datos():
    try:
        data = pd.read_csv("C:/Users/veram/OneDrive/Escritorio/Data Science Henry/FastAPI_OK/dataAPi_7colum.csv")
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Archivo de datos no encontrado")
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=500, detail="El archivo de datos está vacío")
    except pd.errors.ParserError:
        raise HTTPException(status_code=500, detail="Error al parsear el archivo de datos")
    return data




# Endpoint para buscar y mostrar información de una película por su título
@app.get("/titulo/", tags=["Endpoint 1"])
def score_titulo(titulo_pelicula: str = Query(..., description="El título de la película a buscar")):
    # Cargar la base de datos
    data = cargar_datos()

    # Filtrar el DataFrame para encontrar la filmación
    filmacion = data[data['titulo_pelicula'].str.lower() == titulo_pelicula.lower()]

    if filmacion.empty:
        raise HTTPException(status_code=404, detail="película no encontrada")

    # Obtener los datos
    titulo = filmacion['titulo_pelicula'].values[0]
    año = filmacion['year_estreno'].values[0]
    score = filmacion['vote_average'].values[0]

    # Retornar la respuesta
    return {"mensaje": f"La película {titulo} fue estrenada en el año {año} con un score/popularidad de {score}"}



# Endpoint para buscar y mostrar información de una película por su título y votos
@app.get("/votos/", tags=["Endpoint 2"])
def vote_pelicula(titulo_pelicula: str = Query(..., description="El título de la película a buscar")):
    # Cargar la base de datos
    data= cargar_datos()

    # Filtrar el DataFrame para encontrar la película por su título
    data = data[data['titulo_pelicula'].str.lower() == titulo_pelicula.lower()]

    # Verificar si se encontró la película y tiene al menos 2000 valoraciones
    if not data.empty and data["vote_count"].values[0] >= 2000:
        # Extraer información de la película
        titulo = data["titulo_pelicula"].values[0]
        año = data["year_estreno"].values[0]
        votos = data["vote_count"].values[0]
        promedio = data["vote_average"].values[0]

        # Generar mensaje con la información
        mensaje = f"La película {titulo} fue estrenada en el año {año}. Tiene un total de {votos} valoraciones, con un promedio de {promedio:.1f}."
    else:
        # Mensaje si no se encontró suficiente información
        mensaje = f"No hay suficiente información sobre la película {titulo_pelicula}. Se requieren al menos 2000 valoraciones para procesar la solicitud."

    return mensaje




# Función adaptada para contar películas estrenadas en un día específico en español
def cantidad_estrenos_dia(data, dia):
    # Convertir el nombre del día a minúsculas para comparación
    dia_buscar = dia.lower()
    
    # Lista de días válidos en español
    dias_validos = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
    
    # Verificar si el día ingresado es válido
    if dia_buscar not in dias_validos:
        raise HTTPException(status_code=400, detail="El día ingresado no es válido. Debe ser uno de: " + ", ".join(dias_validos))
    
    # Filtrar el DataFrame para encontrar las películas estrenadas en el día especificado
    peliculas_en_dia = data[data['dia_semana'].str.lower() == dia_buscar]
    
    # Contar la cantidad de películas encontradas
    cantidad = peliculas_en_dia.shape[0]
    
    return cantidad

# Endpoint en FastAPI para consultar la cantidad de películas estrenadas en un día específico
@app.get("/cantidad_estrenos_por_dia/" , tags=["Endpoint 3"])
def estrenos_por_dia(dia: str = Query(..., description="Día de la semana en español")):
    # Cargar los datos
    data = cargar_datos()
    
    # Obtener la cantidad de películas para el día especificado
    cantidad = cantidad_estrenos_dia(data, dia)
    
    return {"La cantidad de estrenos en el dia solicitado fue": cantidad}



# Función para contar películas estrenadas en un mes específico
def cantidad_estrenos_mes(data, mes):
    # Convertir el nombre del mes a minúsculas para comparación
    mes_buscar = mes.lower()
    
    # Lista de meses válidos en español
    meses_validos = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    
    # Verificar si el mes ingresado es válido
    if mes_buscar not in meses_validos:
        raise HTTPException(status_code=400, detail="El mes ingresado no es válido. Debe ser uno de: " + ", ".join(meses_validos))
    
    # Filtrar el DataFrame para encontrar las películas estrenadas en el mes especificado
    peliculas_en_mes = data[data['mes_estreno'].str.lower() == mes_buscar]
    
    # Contar la cantidad de películas encontradas
    cantidad = peliculas_en_mes.shape[0]
    
    return cantidad

# Endpoint en FastAPI para consultar la cantidad de películas estrenadas en un mes específico
@app.get("/cantidad_estrenos_por_mes/", tags=["Endpoint 4"])
def estrenos_por_mes(mes: str = Query(..., description="Mes del estreno en español")):
    # Cargar los datos
    data = cargar_datos()
    
    # Obtener la cantidad de películas para el mes especificado
    cantidad = cantidad_estrenos_mes(data, mes)
    
    return {"cantidad_estrenos en el mes solicitado fue": cantidad}


# Iniciar la aplicación con Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
