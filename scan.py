#!/usr/bin/env python
import subprocess
import sys

def ejecutar(ip, first, last):

	global files
	sh = open("ports.sh", "r")
	read_sh = sh.read()
	files = subprocess.run([read_sh, ip, first, last], capture_output=True, text=True)
	print(files.stdout, end="")

def txt():
	global ports
	ports = files.stdout
	global port
	port = ports.split()
	with open("Puertos.txt", "w") as file:
		for i in range(0, len(port), 2):
			file.write('Puerto ')
			file.write(port[i])
			file.write(' abierto')
			file.write('\n')
