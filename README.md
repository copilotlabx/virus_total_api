Proyecto: Verificación y Análisis de Archivos con VirusTotal API

Este proyecto en Python está diseñado para facilitar la verificación y el análisis de archivos utilizando la API pública de VirusTotal. 
El objetivo principal es identificar archivos potencialmente maliciosos y asegurar la integridad y seguridad del entorno local.
A continuación se detallan las características principales del proyecto:
Funcionalidades

    Conexión con la API de VirusTotal:
        El proyecto establece una conexión segura con la API de VirusTotal mediante una clave de API específica del usuario.

    Listado de Archivos:
        Lista todos los archivos presentes en un directorio especificado (por defecto, la carpeta "en_cuarentena").
        Muestra los archivos en la consola para que el usuario pueda seleccionar cuál analizar.

    División de Archivos Grandes:
        Los archivos que superan los 400MB se dividen en fragmentos más pequeños para cumplir con las restricciones de tamaño de la API de VirusTotal.
        Los fragmentos se almacenan en una subcarpeta denominada "fragmentos".

    Análisis de Archivos:
        Permite al usuario seleccionar un archivo para su análisis.
        Calcula el hash MD5 del archivo o de sus fragmentos y obtiene el reporte correspondiente de VirusTotal.
        Verifica el reporte para determinar si el archivo es malicioso o seguro basándose en el número de detecciones positivas.

    Manejo de Errores y Respuestas de la API:
        Maneja adecuadamente las distintas respuestas de la API (200, 204, 400, 403) y proporciona mensajes claros para cada caso.
        Incluye tiempos de espera (rate limiting) para evitar exceder el número de peticiones permitido por la API.

Uso del Proyecto

    Configuración Inicial:
        Asegúrate de tener una clave de API de VirusTotal y configúrala en el script.
        Coloca los archivos a analizar en la carpeta "en_cuarentena".

    Ejecución del Script:
        Ejecuta el script en Python.
        Selecciona el archivo a analizar de la lista mostrada.
        El script dividirá y analizará los archivos grandes, mostrando los resultados en la consola.

    Interacción:
        El usuario puede continuar analizando archivos hasta que decida salir ingresando 'q'.

Requisitos

    Python 3.x
    Biblioteca hashlib para el cálculo de hashes.
    Biblioteca os para la manipulación de archivos y directorios.
    Biblioteca time para manejar tiempos de espera.
    Biblioteca virus_total_apis para interactuar con la API de VirusTotal.

Ejemplo de Uso

    Coloca los archivos sospechosos en la carpeta "en_cuarentena".
    Ejecuta el script y selecciona un archivo de la lista.
    Revisa los resultados del análisis en la consola.

Beneficios

    Automatiza el proceso de análisis de archivos utilizando la potente base de datos de VirusTotal.
    Facilita la gestión y verificación de archivos grandes mediante su fragmentación.
    Proporciona una interfaz sencilla y clara para el usuario final.
