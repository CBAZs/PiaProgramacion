

#LibPY
import json
import os
from datetime import datetime               #Archivo a leer, IP, API, ruta imagenes, numeros, compañia
from hashlib import md5
#LibLocales
import archivos
import Hunter
import metadata
import analizador_urls

#LibTerceros
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
from virus_total_apis import PublicApi
from pyhunter import PyHunter
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-tool", help="Herramienta a usar: Analizar_URLs/ Hunter/ Analizar_archivos/  Metadata/ Scanner ", type=str, required= True)
    parser.add_argument("-comp", help="Compania donde se buscarán los correos", type=str)
    parser.add_argument("-num", help="Numero de correos a buscar", type=int, default=1)
    parser.add_argument("-api", help=".txt Donde tengas escrita tu APIkey", type=str)
    parser.add_argument("-dir", help="Ruta de la carpeta de imagenes o URLs, o ruta del archivo a analizar", type=str)
    params = parser.parse_args()
    
    herramienta = params.tool.lower()

    if herramienta == "hunter":
        open_api_file = open(params.api, "r")
        api_file = open_api_file.read()
        Hunter.hunter_mail(api_file ,params.comp, params.num)
    elif herramienta == "metadata":
        metadata.decode_gps_info
        metadata.get_exif_metadata
        metadata.printMeta(params.dir)
    elif herramienta == "analizar_archivos":
        open_api_file = open(params.api, "r")
        api_file = open_api_file.read()
        archivos.archivo(params.dir, api_file)
    elif herramienta == "analizar_urls":
        open_api_file = open(params.api, "r")
        api_file = open_api_file.read()
        analizador_urls.analizar(api_file, params.dir)
    else:
        print("")