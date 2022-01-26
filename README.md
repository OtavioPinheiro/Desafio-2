<a href="https://github.com/OtavioPinheiro/Desafio-1/blob/master/LICENSE.md" alt="LICENSE">
<img src="https://img.shields.io/badge/LICENSE-MIT-brightgreen"/></a>
<a href="" alt="FullCycle">
<img src="https://img.shields.io/badge/Desafio-FullCycle-yellow"/></a>
<a href="" alt="DOCKER">
<img src="https://badgen.net/badge/icon/docker?icon=docker&label"/></a>

[![](https://badgen.net/github/commits/OtavioPinheiro/Desafio-1)](https://github.com/OtavioPinheiro/Desafio-1/commits)
[![](https://img.shields.io/badge/Python-62%25-green)]()

# Desafio 2 do PFA :whale: :snake:
Primeiro desafio do PFA do curso *Full Cycle*.

# Sumário
- [Descrição](#descrição)
- [Dicas](#dicas)
- [Execução](#execução-dos-containers)
- [Observações](#observações)

## Descrição
Aproveite o desafio 1 que você criou no PFA, a aplicação com sua linguagem favorita, Nginx e MySQL para aplicar o Docker Compose.

Crie o docker-compose.yaml com 3 serviços, um para cada tecnologia. Você deverá configurar os seguintes pontos:

- O serviço do MySQL não poderá ter um Dockerfile personalizado, é necessário usar diretamente a imagem oficial do MySQL e deverá existir um volume para persistir o banco de dados no projeto, o nome da pasta será dbdata. Deverá usar o entrypoint-initdb.d para já criar um banco e popular dados no banco de dados padrão.

- O serviço da sua linguagem favorita deverá continuando a listar dados através da WEB vindo do MySQL. Antes do container iniciar ele deverá verificar se o MySQL já está pronto para conexão, sugerimos usar o Dockerize para fazer esta verificação.

- O serviço do Nginx continuará sendo um proxy reverso para a sua aplicação da linguagem favorita e deverá expor a porta 8000 para acessar a aplicação no browser. Este serviço deverá iniciar somente quando o da sua aplicação da linguagem favorita for iniciado e deverá ser reiniciado automaticamente caso a aplicação da linguagem favorita não esteja rodando ainda.

- Os serviços do MySQL e da linguagem favorita devem ter uma rede compartilhada que o Nginx não enxergue e linguagem favorita e Nginx devem ter uma rede compartilhada que o MySQL não enxergue.

Para corrigir seu projeto rodaremos apenas o comando "docker-compose up", tudo já deve ser levantado e estar disponível ao fazer isto, teste bastante isto antes de enviar o desafio para correção.

Divirtam-se e bom trabalho!

# Dicas
## MySQL
- O arquivo init.sql é bem útil quando queremos criar um banco dados de uma forma mais específica e controlada. Nele podemos especificar o *Database* diretamente por do `CREATE DATABASE <nome_do_database>`, sem precisar fazer essa tarefa por meio de comando quando executarmos o `docker run -e MYSQL_DATABASE=<nome_do_database>` ou pelo Dockerfile `ENV MYSQL_DATABASE <nome_do_database>`, ambos os casos definindo a variável de ambiente MYSQL_DATABASE=<nome_do_database>. Outra vantagem é que já podemos criar a tabela e popula-la utilizando o próprio SQL para isso. Utilizando a estratégia do init.sql temos que copiá-lo para dentro da imagem utilizando o compartilhamento de volumes do docker-compose, isso irá copiar o arquivo init.sql para a pasta docker-entrypoint.init.d e quando o banco de dados for iniciado pela primeira vez, ele irá executar todos os arquivos .sql que estão dentro desta pasta em ordem crescente, 0 a 9, A a Z.

## Flask
- No código Python, não precisaremos criar e nem popular os dados na tabela do MySQL porque o arquivo init.sql já se encarregará disso. Só precisamos então, conectar com o banco de dados.

## Nginx
- Configurar o arquivo default.conf adequadamente.
- Compartilhar a porta correta quando executar o *container*, nesta aplicação foi utilizado o `ports` do docker-compose.

## Docker-compose
### Dockerize
- Dockerize é uma ferramenta que serve, basicamente, para controlarmos a subida de um serviço. No arquivo docker-compose, quando passamos o entrypoint no serviço flask, não foi necessário informar o docker-entrypoint.sh, então a instrução ficou assim: `dockerize -wait tcp://db:3306 -timeout 30s`

# Execução dos *containers*
Para executar essa aplicação, após ter realizado o `git clone`, basta rodar o seguinte comando:
- `docker-compose up -d`