# 201901-PlacaSMD-Geral
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### Placa SMD

Esta aplicação consiste no sistema para o gerenciamento do projeto Estação de Solda, destinado a disciplina Projeto Integrador 2. 

### Contribuição
Você quer contribuir com nosso projeto? É simples! Temos um [guia de contribuição](CONTRIBUTING.md) onde são explicados todos os passos para contribuir. Ahh, não esquece de ler nosso [código de conduta](CODE_OF_CONDUCT.md).
Caso reste duvidas você também pode entrar em contato conosco criando uma issue ou pelo email gustavomn93@gmail.com
Para contribuir com as outras aplicações do nosso sistema, acesse nossa organização:[Estação de Solda](https://github.com/pi2-2019)

### Ambiente

## Pré-Requisitos 
* Python atuliazado
* Virtualenv atualizado

Para montar o ambiente do projeto é necessário a ter instalado o virtualenv. 
Após ter baixado o projeto, copiar a pasta pi2 para fora do projeto.

## Banco de dados

Ter instalado o PostgreSQL, criar a base de dados chamada unidadecentral e criar um usuário chamado admin com a senha 'admin'.

## Entrar no ambiente virtual

Executar o comando source 'caminho da pasta pi2'/bin/activate pelo terminal. 
Após a execução deste comando, o terminal irá ser modificado, constando a palavra "(pi2)" na frente da linha de execução

## Executando as Migrações

No terminal, digitar os comandos: 
```
$ pip install requirements.txt
```

```
$ python manage.py makemigrations
```

```
$ python manage.py maigrate
```

## Executando o projeto

```
$ python manage.py runserver
```

# Enviando o Gcode para o microcontrolador MSP430

* Entrar na pasta EnviarGcode
* No terminal digitar o comando: 

```
$ python send_gcode.py -p /dev/ttyACM0 -f 'Diretório do Gcode'
```
Onde o caminho '/dev/ttyACM0' é o caminho da porta serial
