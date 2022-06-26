import requests
import json
from db.connectionString import api_key


def getNumberFromFile(filename: str, overlay: bool = False, api_key: str = api_key, language: str ='eng') -> str:
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    result_json = json.loads(r.content.decode())

    return result_json['ParsedResults'][0]['ParsedText'].strip('\r\n')