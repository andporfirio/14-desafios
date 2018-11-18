DESAFÍO MERCADO LIVRE 1
Dado um arquivo CSV que contém nome, sobrenome e email de usuários, desenvolver um
sistema que o leia e crie contas e password em OpenLDAP. A senha deve ser do tipo random e
deve ser enviada por email, junto com o nome do usuário. Quando faça login pela primeira vez
deve solicitar a mudança da senha.
O estado de todos os usuários deve ser guardado num banco de dados MySQL ou MongoDB
junto com sua senha armazenada de forma segura.
O desenvolvimento deve ser realizado em Python, Ruby ou Java.


#### Notes ####

Para executar o programa executar o arquivo programa.py

O programa somente irá ser executado em Sistemas Operacionais Linux.

O Programa irá tentar localizar no diretório atual o arquivo .csv, caso nenhum arquivo seja informado o mesmo irá utilizar o arquivo default users.csv, o arquivo .csv devera estar no módelo:

nome;sobrenome;email

Após importar o arquivo o mesmo irá gerar uma conta de acesso combinando o nome e sobrenome e uma senha randomica, que será enviado por email para o email informado no arquivo .csv

Após o envio do email, o programa irá questionar se deseja salvar os dados em uma base de dados, caso a resposta sejá "Y" o mesmo irá solicitar os dados de acesso a base de dados, o mesmo irá tentar conectar em uma base mysql, não existe conexão para outra base de dados.

No final irá ser impresso na tela no formato .ldif, as configurações da conta

