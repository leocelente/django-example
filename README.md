# Django Example

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
