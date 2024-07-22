# Author : Eduardo Esteves - copilotlabxgmail.com
# Perú-2024
import hashlib
from virus_total_apis import PublicApi
import os
import time

# Conexion con la API de Virus Total #La API_KEY es diferente para casa usuario y se obtiene con una cuenta en virustotal.com
API_KEY = 'xyzxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxyzx'
api = PublicApi(API_KEY)

#Verifica y Lista todos los Archivos actuales en las carpeta actual del proyecto "en_cuarentena"

def list_files_in_current_directory(directory):
    # Obtener el directorio actual
    
    
    # Listar todos los archivos en el directorio actual
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Presentar los archivos
    if not files:
        print("No files found in the current directory.")
    else:
        print("Files in current directory:")
        for i, file_name in enumerate(files):
            print(f"{i + 1}: {file_name}")
    
    return files
# Presenta todos los archivos que existen en la carpeta
directory = r"C:\Users\Two\Desktop\virustotal_api\en_cuarentena"
directory_2 = r"C:\Users\Two\Desktop\virustotal_api\en_cuarentena\fragmentos"

files_in_current = list_files_in_current_directory(directory)
# Función para dividir archivos en fragmentos menores a 200MB
def split_file(file_path, output_dir, chunk_size=400 * 1024 * 1024):
    os.makedirs(output_dir, exist_ok=True)
    file_parts = []
    with open(file_path, "rb") as file:
        part_num = 0
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            part_file_path = os.path.join(output_dir, f"{os.path.basename(file_path)}.part{part_num}")
            with open(part_file_path, "wb") as part_file:
                part_file.write(chunk)
            file_parts.append(part_file_path)
            part_num += 1
    return file_parts
 
# Permite al usuario escoger el archivo a Analizar

while True:
    try:
          
            user_input = input("Ingrese el número índice correspondiente del archivo que desea analizar (o 'q' para salir): ")
            if user_input.lower() == 'q':
                print("Saliendo del programa.") 
                break
         
            file_index = int(user_input) -1
          
            if 0 <= file_index < len(files_in_current):
                    file_path = os.path.join(directory, files_in_current[file_index])
                    file_size = os.path.getsize(file_path)

                    RATE_LIMIT_SLEEP_TIME = 60  # tiempo de espera en segundos después de recibir una respuesta 
                   # Permite Fragmentar el archivo a analizar 
                    if file_size > 400 * 1024 * 1024:
                        print("El archivo es mayor a 400MB. Dividiendo en fragmentos...")
                        output_dir = os.path.join(directory, "fragmentos")
                        file_parts = split_file(file_path, output_dir)
                        files_in_fragmentos = list_files_in_current_directory(output_dir)
                
                        print("Analizando los fragmentos en la carpeta 'fragmentos'...")
                        for part in files_in_fragmentos:
                            print("Espera un momento mientras se analiza el fragmento :   " + part)
                            part_path = os.path.join(output_dir, part)
                            with open(part_path, "rb") as file:
                               file_hash = hashlib.md5(file.read()).hexdigest()
                               response = api.get_file_report(file_hash)
                               response_code = response["response_code"]
                            if response_code == 200:  # Informe disponible
                                if 'results' in response and 'positives' in response['results']:
                                      #if response["results"]["positives"] > 10:  # Detecta que no haya ningún positivo, por lo que es malicioso.
                                      print(f"Archivo malicioso: {part_path}")
                                     # print(f"Total en base a Virus Total: {response['results']}") "Para Verificación de un parámetro en específico"
                                     # print(f"Resultados en base a Virus Total: {response['results']['positives']}") "Para Verificación de un parámetro en específico"
                                  #else:
                                   #   print(f"Archivo seguro: {part_path}")  # Si encuentra que no es positivo se imprime esto.
                                
                                else:
                                  print(f"Archivo seguro: {part_path}")  # Si encuentra que no es positivo se imprime esto.
                                # print(f"Total en base a Virus Total: {response['results']}")  "Para Verificación de un parámetro en específico"
                                # print(f"Resultados en base a Virus Total: {response['results']['positives']}")  "Para Verificación de un parámetro en específico"

                                
                                   # print("No se encontraron resultados en el análisis del archivo.")
                            elif response_code == 204:
                                  print("Numero de peticiones exididas.")
                                  time.sleep(RATE_LIMIT_SLEEP_TIME)

                            elif response_code == 400:
                                    print("Mala Peticion.")
                            elif response_code == 403:
                                  print("No cuenta con los permisos revisar API_KEY")
                            else:
                                 print("Código de respuesta desconocido.")
                            
                            time.sleep(60)  # espera 1 minuto por cada fragmento 
                             
                             
                             
                    else:
                       with open(file_path, "rb") as file:
                         file_hash = hashlib.md5(file.read()).hexdigest()
                         response = api.get_file_report(file_hash)
            
           
                       response_code = response["response_code"]
                       if response_code == 200:  # Informe disponible
                          if 'results' in response and 'positives' in response['results']:
                            if response["results"]["positives"] > 10:  # Detecta que no haya ningún positivo, por lo que es malicioso.
                               print(f"Archivo malicioso: {file_path}")
                            #  print(f"Total en base a Virus Total: {response['results']}") "Para Verificación de un parámetro en específico"
                            #  print(f"Resultados en base a Virus Total: {response['results']['positives']}") "Para Verificación de un parámetro en específico"
                            else:
                                print(f"Archivo seguro: {file_path}")  # Si encuentra que no es positivo se imprime esto.
                            #   print(f"Total en base a Virus Total: {response['results']}")  "Para Verificación de un parámetro en específico"
                            #   print(f"Resultados en base a Virus Total: {response['results']['positives']}")  "Para Verificación de un parámetro en específico"
                          else:
                           print("No se encontraron resultados en el análisis del archivo.")
                       elif response_code == 204:
                         print("Numero de peticiones exididas.")
                       elif response_code == 400:
                         print("Mala Peticion.")
                       elif response_code == 403:
                         print("No cuenta con los permisos revisar API_KEY")
                       else:
                         print("Código de respuesta desconocido.")
            else:
               print("Índice fuera del rango. Por favor ingrese un valor válido.")
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número o 'q' para salir.")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {files_in_current[file_index]}. Puede que haya sido movido o eliminado.")
   
