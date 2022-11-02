
from openpyxl import Workbook
import os
import time
import requests
import re
import datetime
import argparse



def analizar(key, ubicacion):

    api_key = str(key)
    urls = open(ubicacion, 'r')
    read_urls = urls.read()
    urls_txt = open("Analizis_Urls.txt", "a")

    api = "https://www.virustotal.com/vtapi/v2/url/report"
    
    pagina_re = re.compile('(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})')
    pagina_e = pagina_re.findall(read_urls)

    for i in range(len(pagina_e)):
        link = pagina_e[i]
        req = requests.get(link)
        
        if req.status_code == 200:
            parametros = {
                'apikey': api_key,
                'resource': link
            }
            analisis = requests.get(api, params=parametros)
            json = analisis.json()
            
            
            if json['positives'] < 3:
                urls_txt.write(f"\n{pagina_e[i]} : Bajo riesgo ")
            elif json['positives'] >= 3 and json['positives'] < 10:
                urls_txt.write(f"\n{pagina_e[i]} : Medio riesgo ")
            else:
                urls_txt.write(f"\n{pagina_e[i]} : Alto riesgo!! ")
        else:
            urls_txt.write("pagina no encontrada :(")
            