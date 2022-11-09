#!/usr/bin/env python
import requests
import os
import json 

class PublicApi():
    def __init__(self, api_key=None, proxies=None):
        self.api_key = api_key
        self.proxies = proxies
        self.base = 'https://www.virustotal.com/vtapi/v2/'
        self.version = 2
        if api_key is None:
            raise ApiError("You must supply a valid VirusTotal API key.")
    
    def _return_response_and_status_code(response, json_results=True):
        if response.status_code == requests.codes.ok:
            return dict(results=response.json() if json_results else response.content, response_code=response.status_code)
        
    def scan_file(self, this_file, from_disk=True, filename=None, timeout=None):
        params = {'apikey': self.api_key}
        if from_disk:
            if not filename:
                filename = os.path.basename(this_file)
            files = {'file': (filename, open(this_file, 'rb').read())}
        else:
            if filename:
                files = {'file': (filename, this_file)}
            else:
                files = {'file': this_file}

        try:
            response = requests.post(
                self.base + 'file/scan', files=files, params=params, proxies=self.proxies, timeout=timeout)
        except requests.RequestException as e:
            return dict(error=str(e))
            return _return_response_and_status_code(response)
