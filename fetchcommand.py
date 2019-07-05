import requests

def fetchcmd():
    url = 'http://taabishm2.pythonanywhere.com/fetch'
    r = requests.get(url, allow_redirects=True)
    resp = r.content.decode('utf-8')
    return resp
