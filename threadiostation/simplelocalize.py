import json
import io
import locale
import os
"""
A simple way to localize the tool.
"""
def localizeToDict(path):
    with open(path) as file:
        return json.loads(''.join(file.read()))

def setupLocalization():
    lang = locale.getdefaultlocale()[0]
    path = './threadiostation/internationalization/' + lang + '.json'
    print(path)
    if os.path.isfile(path):
        return localizeToDict(path)
    else:
        return localizeToDict('./threadiostation/internationalization/en.json')

