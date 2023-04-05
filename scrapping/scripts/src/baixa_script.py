import requests

url = 'https://gist.githubusercontent.com/456789123/2c58ecdf761cf20f9ba1/raw/43b489ba9f7260e042de31d6e1a9a5e0be08f4da/Regi%C3%B5es_Brasil.sql'
response = requests.get(url)

if response.status_code == 200:
    with open(r'scrapping\scripts\arquivos\script.sql', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print("Arquivo salvo com sucesso!")
else:
    print("Não foi possível baixar o arquivo.")
