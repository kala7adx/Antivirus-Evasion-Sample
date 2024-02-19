import base64
import os

#bytes = bytearray("print(dict(__import__('os').environ))", 'utf-8')

#base64string = base64.b64encode(bytes)

#f = open('harmless.py', 'w')

#f.write(base64string.decode('utf-8'))

f = open('harmless.py', 'r')

eval(base64.b64decode(f.readline()).decode('utf-8'))
