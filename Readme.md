# Gerenciamento de Sensores Inteligentes

## Problema 1 - Conectividade e Concorrência

### Autores
<div align="justify">
  <li><a href="https://github.com/Pegasus77-Adriel/Gerenciamento-de-Sensores-Inteligentes.git">@Adriel-Santana</a></li>
</div>

### Máquina
1. Sistema operacional:
  - Windows 10;
  - Ubuntu 22.04 LTS;
2. Linguagem de programação: python:3.11.4;
  - Bibliotecas nativas utilizadas:
    - flask;
    - socket
    - json;
    - request;
    - threading;
    - os
    - datetime
### 

### Instruções
Observação: O docker deve está previamente instalado na máquina.
1. Clone o repositório.
   ```sh
   git clone https://github.com/Pegasus77-Adriel/Gerenciamento-de-Sensores-Inteligentes.git
   ```
2. Abra a pasta atráves do explorador de arquivos da sua máquina.
3. Abra o terminal no diretório
   * Windows, use
   ```sh
   No campo de endereço, digite 'cmd' e pressione Enter
   ```
    * Linux, use
   ```sh
   Clique com o botão direito do mouse em uma área vazia dentro do diretório,
   Selecione "Abrir no terminal" ou uma opção semelhante.
   ```
4. Compile os arquivos com extensão .py do projeto.
* Abra a pasta aplicacao:
     ```sh
     cd aplicacao
     ```
   * Compile o arquivo app.py:
     ```sh
       docker build -t app-1 .
     ```
   * retorne a pasta anterior:
       ```sh
       cd ..
      ```
* Abra a pasta sensores:
     ```sh
     cd sensores
     ```
   * Compile o arquivo dispositivos.py:
     ```sh
       docker build -t sensor-1 .
     ```
   * retorne a pasta anterior:
       ```sh
       cd ..
      ```
* Abra a pasta servidor:
     ```sh
     cd servidor
     ```
   * Compile o arquivo dispositivos.py:
     ```sh
       docker build -t servidor-1 .
     ```
   * retorne a pasta anterior:
       ```sh
       cd ..
      ```
5. Execute os containers docker.
* execute a imagem servidor-1:
     ```sh
     docker run --network=host -it servidor-1
     ```
* execute a imagem sensor-1:
     ```sh
       docker run --network=host -it -e SERVER-IP='coloque o IP da máquina que o container do servidor está rodando' sensor-1
     ```
* execute a imagem app-1:
     ```sh
       docker run --network=host -it -e SERVER-IP='coloque o IP da máquina que o container do servidor está rodando' app-1
      ```
# Gerenciamento inteligente de dispositivos IoT
O propósito central deste sistema é otimizar a comunicação entre diversos dispositivos e suas respectivas aplicações. Isso abrange não apenas a capacidade das aplicações de receber dados remotamente dos dispositivos, mas também de controlar esses dispositivos de forma eficaz. Para alcançar esse propósito, o sistema incorpora protocolos de comunicação como UDP, TCP e HTTP, todos concebidos para assegurar a confiabilidade do serviço.

## 2. Solução do problema
No desenvolvimento do sistema foi utilizado a linguagem de programação Python na versão 3.11.4, bem como as funcionalidades incluídas nas bibliotecas nativas da linguagem, além do framework Flask para implementação da API Rest.

## 2.1 Sensor e Servidor
Para a comunicação do [dispositivos](https://github.com/Pegasus77-Adriel/Gerenciamento-de-Sensores-Inteligentes/blob/main/sensores/dispositivos.py) com o [servidor](https://github.com/Pegasus77-Adriel/Gerenciamento-de-Sensores-Inteligentes/blob/main/servidor/broker.py) foi utilizado o protocolo de comunicação UDP e TCP-IP além de um padrão nas trocas de mensagens, como é descrito no diagrama abaixo:

![diagrama sensor e servidor](https://github.com/Pegasus77-Adriel/Gerenciamento-de-Sensores-Inteligentes/blob/main/diagrama%20servidor%20e%20sensor.png)

## 2.2 Protocolos UDP e TCP
Nesse projeto entre os sensores e o servidor foram utilizados 2 tipos de protocolos de comunicação: 
- Protocolo UDP: é um protocolo de comunicação da camada de transporte que oferece um serviço de entrega de dados rápido e eficiente, mas não garante a entrega ou a ordem dos pacotes. Ele é amplamente utilizado em situações onde a perda ocasional de dados não é crítica, como é o caso do envio de dados dos sensores para o servidor.
- Protocolo TCP-IP: é um protoclo que garante a entrega confiável de dados, verificando e retransmitindo pacotes perdidos. Além disso, o TCP controla o fluxo de dados e adapta a taxa de transmissão para evitar congestionamentos na rede. Sua orientação à conexão estabelece e encerra conexões de forma segura, garantindo a integridade dos dados transmitidos. Essas qualidades tornam o TCP uma escolha amplamente utilizada em aplicações que exigem comunicação confiável e orientada à conexão, por esse motivo esse protocolo foi escolhido para garantir que os comandos enviados pelo servidor sejam entregues de forma confiável para os sensores.
  
A troca de mensagens entre os sensores e o servidor pode ser vista no diagrama anterior, inclusive o padrão de mensagens adotados por eles.
## 2.3 Servidor e Aplicação
Para a comunicação do [servidor](https://github.com/Pegasus77-Adriel/Gerenciamento-de-Sensores-Inteligentes/blob/main/servidor/broker.py) com a [aplicação](https://github.com/Pegasus77-Adriel/Gerenciamento-de-Sensores-Inteligentes/blob/main/aplicacao/app.py) foi utilizado o protocolo de comunicação HTTP através da implementação da API Rest, como pode ser visto no diagrama abaixo:
![diagrama servidor e app](https://github.com/Pegasus77-Adriel/Gerenciamento-de-Sensores-Inteligentes/blob/main/diagrama%20servidor%20e%20app.png)

## 2.4 protocolo HTTP e API Rest
- HTTP: é o protocolo usado para comunicação na web, que opera em um modelo cliente-servidor, onde o cliente faz requisições ao servidor, que responde com os dados solicitados. Geralmente utiliza os métodos de requisição como GET e POST, que são usados para receber e enviar dados pro servidor.

