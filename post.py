import requests

urlPOST = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=848691f4f1b54082283859587284b3f62466d6fe';

# ENVIAR POST PARA O SERVIDOR
r = requests.post(urlPOST, 
files={"answer": open("answer.json", "rb")})

print(r.text)