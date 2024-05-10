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
Observação: O docker deve está previamente instalado na maquina.
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
  
