

Sistema de Recomendación y Análisis de Datos de Películas

Este proyecto implementa un sistema de recomendación y análisis de datos de películas utilizando técnicas de procesamiento de datos y algoritmos de recomendación. El objetivo principal es proporcionar recomendaciones personalizadas de películas basadas en similitudes entre películas y análisis de datos detallados.


Algoritmo de Recomendación
El sistema utiliza un enfoque basado en contenido y colaborativo para generar recomendaciones:

Preprocesamiento de Datos:

Carga de datos desde una base de datos o archivo CSV.
Limpieza de datos para eliminar valores nulos y datos inconsistentes.
Creación de Características:

Extracción de características relevantes como género, director, actores principales, y más.
Cálculo de Similitud:

Utilización de técnicas como la similitud coseno o la matriz de similitud para calcular la cercanía entre películas basadas en sus características.
Generación de Recomendaciones:

Identificación de películas similares a la película seleccionada por el usuario basada en la similitud calculada.
Análisis de Base de Datos
El sistema también proporciona capacidades de análisis exploratorio de datos (EDA) para entender mejor las características y patrones dentro de la base de datos de películas:

Visualización de Datos: Gráficos y visualizaciones para explorar distribuciones de género, popularidad por año de estreno, y más.

Estadísticas Descriptivas: Análisis de tendencias, conteos de películas por género, y otros medidas.

Uso del Proyecto
Para utilizar el proyecto, sigue estos pasos:

Instalación de Dependencias:

Asegúrate de tener Python y las bibliotecas necesarias instaladas (pandas, numpy, scikit-learn, etc.).
Configuración de Datos:

Carga tus datos de películas en el formato adecuado (CSV, base de datos) y asegúrate de que estén accesibles para la aplicación.
Ejecución del Sistema:

Inicia la aplicación y utiliza los endpoints proporcionados para obtener recomendaciones o realizar análisis de datos.
Tecnologías Utilizadas
Python: Lenguaje de programación principal.
FastAPI: Framework web utilizado para construir endpoints RESTful.
Pandas y NumPy: Librerías para manipulación y análisis de datos.
Scikit-learn: Utilizado para cálculos de similitud y modelos de aprendizaje automático si es aplicable.
