import json
import io
import locale
import os
"""
A simple way to localize the tool.
"""
def localizeToDict(path):
    with open(path, encoding='utf-8') as file:
        return json.loads(''.join(file.read()))

def setupLocalization():
    lang = locale.getdefaultlocale()[0]
    path = './internationalization/' + lang + '.json'
    if os.path.isfile(path):
        return localizeToDict(path)
    else:
        return localizeToDict('./internationalization/en.json')

