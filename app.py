from flask import Flask, request
import requests

api = Flask(__name__)
api.config["DEBUG"] = True

# una route vera, che non sia una richiesta api, ci va se no il deploy va in errore
@api.route('/')
def hello_world():
    return 'Hello, World!'

  
r = requests.get('https://drive.google.com/open?id=1t-nlUvbtD6ungcj0I_BweubRnbUogjVG')
with open('downloaded_files/modelarch.json', 'wb') as f:
    f.write(r.content)
    
if __name__ == '__main__':
   api.run(host='127.0.0.1', port=5000)
