import json
import requests
#login

def login(usuario, senha):
     valor = {'username':usuario,'password':senha}
     r=  requests.post('http://127.0.0.1:8000/api-token-auth/',valor)
     #pegar token do usuario e converter para jason
     t= json.loads(r.text)
     autenticar ='Token '+t['token']
     head = {"Authorization":autenticar}
     print(head)
     return head
     

def get_dados(nome_url):
    #pegar dados logado
    r= requests.get('http://127.0.0.1:8000/'+nome_url+'/',headers=login('pe','Senha123@'))
    tudo = json.loads(r.content)#retorna todos os dados em json
    for i in tudo:
        print(i)
#chama a funçao de mostrar dados
get_dados('usuarios')        

'''
exemplos de deletar atualizar etc...
valores = {'linha1': 'endereço test244',
           'cidade':'Brusque','estado':'SP','pais':'Brasil'}

valores = {'cidade':'Jordania'}
#r = requests.get("http://127.0.0.1:8000/get", params=payload)
#r = requests.get("http://127.0.0.1:8000/pontoturistico/13/")
#r = requests.delete('http://127.0.0.1:8000/pontoturistico/13/')
#r = requests.post('http://127.0.0.1:8000/enderecos/', data=valores)
r = requests.patch('http://127.0.0.1:8000/enderecos/2/', data=valores)
print (r.url)
print(r.text)
input("aperte enter para sair")

head = {"Authorization":"Token token=xxxxxxxxxxxxxxxxxxxxxx"}
url = 'http://0.0.0.0:3000/api/v1/update_experiment.json'
payload = {'expt_name' : 'A60E001', 'status' : 'done' }

r = requests.patch(url, payload, headers=head)
'''
