import subprocess
import requests


def archivos(file, apikey):

    hash = subprocess.check_output(["md5",file]) 
    hash = hash.split()
    hash = hash[3]
    hash = hash.decode() 

    fileHash = str(hash)
    params = {}
    
    apiKey = str(apikey)
    params = {'apikey': apiKey, 'resource': fileHash}

    responseData = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)

    jsonData = responseData.json()
    responseData = int(jsonData.get('response_code'))
    f = open("resultados.txt", 'w')
    if(responseData == 0):
        f.write('\nEl archivo con el hash: ' + fileHash + ' no fue encontrado en virustotal\n')
    elif(responseData == 1):
        if(int(jsonData.get('positives'))) == 0:
           f.write('\nEl archivo con el hash ' + fileHash + ' no es un malware\n')
        else:
            f.write('\nCUIDADO! El archivo con el hash: ' + fileHash + ' es un MALWARE!!\n')
    else:
        f.write('\nNo se pudo buscar, intente de nuevo.\n')
