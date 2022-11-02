from hashlib import md5 
import json
from virus_total_apis import PublicApi

def archivo(file, api_key):
    api_key = "[ ]"
    api = PublicApi(api_key)
    with open(file, "rb") as f:
        file_hash = md5(f.read()).hexdigest()
        response = api.file(file_hash) 
        with open("response.json", "w") as f:
            json.dump(response, f, indent=4)
            results = open("resultados.txt", "w")
            
            if response["response_code"] == 200:
                if response["results"]["positives"] > 0:
                    results.write("Archivo malicioso.")
                else:
                    results.write("Archivo seguro.")
            else:
                results.write("No se obtuvo el analisis del archivo.")