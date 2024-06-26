import threading
import socket
import json
from time import sleep
from flask import Flask, request, jsonify

app = Flask(__name__)
class Broker:
  
    def __init__(self):
        
        self.HOST = socket.gethostbyname(socket.gethostname())
        self.UDP_PORT= 60000
        self.TCP_PORT= 59999
        self.BUFFER_SIZE = 2048
        self.dispositivos = []
        self.dados_dispositivos = []
    
    def setDispositivos(self,dados):
        self.dispositivos[dados['matricula']] = str(dados)

    # Start api-REST
    def rest(self,app):
        
        app.run(self.HOST, port = 59998)
        
    # Função main resposável por iniciar as conexões e as threads
    def main(self,rest):
        
        
        try:
            socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
            socket_udp.bind((self.HOST, self.UDP_PORT))
            socket_tcp.bind((self.HOST, self.TCP_PORT))
            socket_tcp.listen()
            
        
            print("Broker iniciado com sucesso!")
                
        except:
            return print("Erro ao iniciar o Broker!")
        
    
        thread1 = threading.Thread(target=self.receber_dados, args=[socket_udp])
        thread1.start()
        thread2 = threading.Thread(target=self.conexaoTCP, args=[socket_tcp])
        thread2.start()
        
        thread3 = threading.Thread(target=self.rest, args=[rest])
        thread3.start()

        
    #Função reponsável receber os dados dos sensores via UDP, e amarzena-los no buffer de dados do broker
    def receber_dados(self, socket_udp):
        
        while True:
            # Recebe os dados dos dispositivos através da conexão UDP
            dados_udp, HOST_client_udp = socket_udp.recvfrom(self.BUFFER_SIZE)
            msg = dados_udp.decode()
            msg = json.loads(msg)
            
            try:
                matricula = int(msg["matricula"])
                self.dados_dispositivos[matricula-1] = msg
            except:
                self.dados_dispositivos.append(msg)
            
            for i in self.dados_dispositivos:
                print(f'{i}')
            
            
    #Função reponsável enviar os comandos para os sensores via TCP-IP 
    def conexaoTCP(self, socket_tcp):
        cont = 0
        while True:
            
            # Aceita a conexão com os sockets dos clientes
            conn_client_tcp, addr_client_tcp = socket_tcp.accept()
            self.dispositivos.append(conn_client_tcp)
            print("Conectado com um cliente TCP em: ", addr_client_tcp)
            cont += 1
            
            dic_dados = {"fonte": "broker", "tipo": "registro","matricula": cont }
            dic_dados_bytes = json.dumps(dic_dados).encode('utf-8')
            conn_client_tcp.sendall(dic_dados_bytes)
            
    #Rota responsável por receber a solicitação vinda da aplicação para alterar o tempo de amostragem dos sensores   
    @app.route('/alterar_temp_amostragem/<segundos>/<matricula>', methods=['GET'])      
    def alterar_temp_amostragem(segundos,matricula):
        
            dispositivo = broker.dispositivos[int(matricula)-1]
            dic_dados = {"fonte": "app", "tipo": "amostragem","tempo":segundos}
            dic_dados_bytes = json.dumps(dic_dados).encode('utf-8')
            dispositivo.sendall(dic_dados_bytes)
            sleep(2)
            dispositivo_dados = broker.dados_dispositivos[int(matricula)-1]
            msg = f'O dispositivo com a matricula {matricula} está com o tempo de amostragem: {dispositivo_dados["intervalo_envio"]}'
            return jsonify({"mensagem":msg}), 200
        
        
           
    #Rota responsável por receber a solicitação vinda da aplicação para alterar o status do dispositivo "ligado" ou "desligar" 
    @app.route('/enviar_comando/<comando>/<matricula>', methods=['GET'])      
    def enviar_comando(comando,matricula):
        try:
            dispositivo = broker.dispositivos[int(matricula)-1]
            dic_dados = {"fonte": "app", "tipo": "comando","operacao":comando}
            dic_dados_bytes = json.dumps(dic_dados).encode('utf-8')
            dispositivo.sendall(dic_dados_bytes)
            sleep(2)
            dispositivo_dados = broker.dados_dispositivos[int(matricula)-1]
            msg = f'O dispositivo com a matricula {matricula} está {dispositivo_dados["status"]}'
            return jsonify({"mensagem":msg}), 200
        
        except:
            return jsonify({"mensagem": "Falha na operação"}), 200

    #Rota responsável por receber a solicitação vinda da aplicação para requirir a amostragem de um sensor especifico
    @app.route('/receber_medicao/<matricula>', methods=['GET'])
    def receber_medicao(matricula):
        
        try:
            dados = broker.dados_dispositivos[int(matricula)-1]
            return jsonify(dados)
        except:
            return jsonify({"mensagem": "Medição não encontrada!"}), 200
    


broker = Broker()

broker.main(app) 

