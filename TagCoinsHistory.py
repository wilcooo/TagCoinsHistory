from  urllib.request import urlopen
from urllib.parse import urlencode
from json import loads as jsondecode
from time import time

EventSourceURL = 'http://tagpro.lol/stream/updates'
DataDropURL = 'https://script.google.com/macros/s/AKfycbznkUUI6B9nPjgU9XCBSPFdYwBqNEv3fv6nQc79YrDGZOkdhfaP/exec'

# Open the connection to the Event Source
es = urlopen( EventSourceURL )

while True:
    try:

        line = [_.strip() for _ in es.readline().decode('utf-8').split(':',1)]

        if line[0] == 'data' and line[1] != '"connected"':

            datalist = jsondecode( line[1] )

            for data in datalist:
                params = urlencode( data )
                result = urlopen( DataDropURL + '?' + params )
                print( 'Data sent. id:', data['id'] )

    except Exception as e: print('Error:', e)
