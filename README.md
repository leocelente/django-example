# Django Example

## Não rodar fora de desenvolvimento
Eu commitei diretamente a chave secreta que o django usa pra criptografar 
quase tudo. Então seria um risco de segurança grave caso este projeto fosse 
público. **Antes de colocar em algo como o Heroku, trocar a `SECRET_KEY` por 
uma referência a um arquivo de configuração local tipo `.env`, devidamente
adicionado no `.gitignore`
## Executar
Primeiro, crie um ambiente virtual de Python 3.8 ou maior.
```shell
$ virtualenv .venv
$ source .venv/bin/activate
```

Dentro do virtualenv, instale as dependencias: 
```shell
(.venv) $ pip3 install -r requirements.txt
```

Finalmente, podemos rodar o servidor de desenvolvimento:
```shell
(.venv) $ cd top_level_project
(.venv) $ python3 manage.py runserver 
```
