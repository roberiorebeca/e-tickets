# Rest

## Significado

O significado da sigla é, **Representative State Transfer** ou seja **Transferencia de Estado Representacional**. Trata-se de uma abstração da arquitetura da Web. Resumidamente, o REST consiste em princípios/regras/constraints que, quando seguidas, permitem a criação de um projeto com interfaces bem definidas.

O Rest é um estilo arquitetural para aplicações Web, apresentado por Roy Fielding, em 2000, na sua tese Architectural Styles and the Design of Network-based Software Architectures.

Em termos gerais uma aplicação que utiliza o REST disponibiliza métodos, geralmente pelo protocolo HTTP que agirão no servidor, modificando ou obtendo informações, ou seja, a implementação de um CRUD que é feita a partir de uma abstração que utiliza os comandos do próprio protocolo HTTP. Assim o comando POST é usado para criar um novo objeto, o GET para recuperar um ou mais objetos, o PUT para atualizar um objeto já existente e o DELETE para removê-lo.

Existe uma certa confusão quanto aos termos REST e RESTful. Entretanto, ambos representam os mesmo princípios. A diferença é apenas gramatical. Em outras palavras, sistemas que utilizam os princípios REST são chamados de RESTful.

- REST: conjunto de princípios de arquitetura
- RESTful: capacidade de determinado sistema aplicar os princípios de REST.

Geralmente, quando usamos o termo RESTful, estamos nos referindo a um aplicativo que implementa o design de arquitetura REST. No contexto do desenvolvimento da Web, geralmente quando estamos falando de uma API RESTful, estamos nos referindo a serviços da Web (ou APIs da Web). É uma maneira comum de expor partes do seu aplicativo a terceiros (aplicativos externos e sites da Web)

## JSON

Arquivo padrão de comunicação Javascript Object Notation - Notação de Objetos JavaScript

## Verbos (Métodos) utilizados no REST

### GET

O verbo GET é utilizado quando se deseja extrair/buscar uma informação do Banco de Dados/API

### POST

O verbo POST é utilizado quando se deseja salvar/enviar uma informação do Banco de Dados/API

### PUT

O verbo PUT é utilizado quando se deseja atualizar uma informação do Banco de Dados, lembrando que o PUT exige que seja enviado os dados de todos campos

### PATCH

Este verbo é utilizado quando precisamos atualizar um campo especifico de uma tabela
