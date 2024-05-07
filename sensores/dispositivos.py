import socket
import json
import threading
from random import randint
from datetime import datetime
from time import sleep
import os



class Dispositivo:
    
    def __init__(self):
            # Gera um número aleatório de 2 dígitos para a matrícula
            self.matricula = randint(1, 99)
            # Status significa se o dispositivo está ligado ou desligado 
            self.status = "Ligado"
            self.matricula = None
            self.temperatura = 35
            self.umidade = 50 
            self.HOST = '127.0.0.1'
            self.UDP_PORT = 60000
            self.TCP_PORT= 59999
            self.intervalo_envio = 10
            self.BUFFER_SIZE = 2048
            self.socket_udp = None
            self.socket_tcp = None
            self.monitorar = False
            #self.client_udp_rec = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
    def main(self):
        try:
            socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_udp = socket_udp
            self.socket_tcp = socket_tcp
            
            
        except:
           return print("Falha na inicialização do dispositivo")
       
        print("Dispositivo conectado com sucesso!")
        thread1 = threading.Thread(target=self.enviar_dados, args=[socket_udp])
        thread1.start()
        thread2 = threading.Thread(target=self.conexaoTCP, args=[socket_tcp])
        thread2.start()
        
    
    def conexaoTCP(self, socket_tcp):
        socket_tcp.connect((self.HOST,self.TCP_PORT))
        
        while (sair == False):
            mensagem = socket_tcp.recv(self.BUFFER_SIZE)
            dados = mensagem.decode('utf-8')
            if not dados:
                pass
            else:
                print("Mensagem recebida:", dados)
                dados = json.loads(dados)
                self.tratar_comandos(dados)
                
    def tratar_comandos(self, dados):
       
        if (dados["fonte"] == "broker" and dados["tipo"] == "registro"):
            self.matricula = dados["matricula"]
            
            print(f'Dispositivo inicializado com sucesso!')
            
        elif (dados["fonte"] == "app" and dados["tipo"] == "comando"):
            self.setStatus(dados["operacao"])

        elif (dados["fonte"] == "app" and dados["tipo"] == "amostragem"):
            self.setAmostragem(dados["tempo"])
            
    
    def enviar_atualizacao(self):
        
        data_hora_atuais = datetime.now()
        data_hora = data_hora_atuais.strftime('%d-%m-%Y %H:%M:%S')

        dic_dados = { "matricula" : self.matricula, "status" : self.status, "temperatura": str(self.temperatura) +'°C' ,"umidade":str(self.umidade) + '%',
                    "intervalo_envio":self.intervalo_envio, "data_hora" : data_hora}
        
        dic_dados_bytes = json.dumps(dic_dados).encode('utf-8')
                
        self.socket_udp.sendto(dic_dados_bytes, (self.HOST, self.UDP_PORT))
        
        
    def setStatus(self, status):
        
        if(status == "desligar"):
            self.status = "Desligado"
            
        elif(status == "ligar"):
            self.status = "Ligado"
        
        dispositvo.enviar_atualizacao()
        
        print(f'Status do dispositivo atualizado para {self.status}!')
    
    def setAmostragem(self,segundos):
        
        self.intervalo_envio = int(segundos)
        dispositvo.enviar_atualizacao()
        
        print(f'Tempo de amostragem do dispositivo atualizado para {self.intervalo_envio}!')
        
    def dados_atuais(self):
        
        data_hora_atuais = datetime.now()
        data_hora = data_hora_atuais.strftime('%d-%m-%Y %H:%M:%S')
        dic_dados = { "matricula" : self.matricula, "status" : self.status, "temperatura": str(self.temperatura) +'°C' , "umidade":str(self.umidade) + '%',
                              "intervalo_envio":self.intervalo_envio, "data_hora" : data_hora}
        print(dic_dados)
        
        
    def setTemperatura(self):

        n = randint(1,2)
        temp = randint(0,3)
        
        if(n == 1):
            temp = temp * (-1)   
        
        self.temperatura = self.temperatura + (temp)
    
    def setUmidade(self):
        
        n = randint(1,2)
        umidade = randint(0,6)
        
        if(n == 1):
            umidade = umidade * (-1)   
        
        self.umidade = self.umidade + (umidade)
    
       
    def enviar_dados(self, client_env):
        
        while(sair == False):
            sleep(self.intervalo_envio)
            if(self.status == "Ligado"):
            
                dispositvo.setTemperatura()
                dispositvo.setUmidade()
                data_hora_atuais = datetime.now()
                data_hora = data_hora_atuais.strftime('%d-%m-%Y %H:%M:%S')
                
                dic_dados = { "matricula" : self.matricula, "status" : self.status, "temperatura": str(self.temperatura) +'°C' , "umidade":str(self.umidade) + '%',
                              "intervalo_envio":self.intervalo_envio, "data_hora" : data_hora}
                dic_dados_bytes = json.dumps(dic_dados).encode('utf-8')
                
                client_env.sendto(dic_dados_bytes, (self.HOST, self.UDP_PORT))
                
            
            

def exibir_opcoes():
    print("\n===== Bem-vindo ao Menu =====\n")
    print("Escolha uma das opções abaixo:")
    print("1. Ligar sensor")
    print("2. Desligar sensor")
    print("3. Alterar tempo de amostragem ")
    print("4. Solicitar dados atuais")
    print("5. Sair\n")
    

def verificar_numero(numero):
    
    try:
        numero = int(numero)
        return True
    
    except:
         return False

sair = False
dispositvo = Dispositivo()
dispositvo.main()
sleep(5)

while(sair == False):
       exibir_opcoes()
       
       try:
            entrada = input("Digite um número:\n")
            numero = int(entrada)
            
            
            if(numero > 5 or numero <= 0):
                
                    print("Entrada inválida! Por favor, digite um número válido.")
        
            
            elif(numero == 1):
                
                os.system('clear')
                dispositvo.setStatus("ligar")
                
            
            elif(numero == 2):
                
                os.system('clear')
                dispositvo.setStatus("desligar")
                
                    
            elif(numero == 3):
               
                segundos = input("Digite o intervalo de envio em segundos:\n")
                   
                if(verificar_numero(segundos)):
                       
                    dispositvo.setAmostragem(segundos)
                        
                else: 
                       print(f"Tempo digitado '{segundos}' não reconhecido!")
            
            elif(numero == 4):
                dispositvo.dados_atuais()
            
            elif(numero == 5):
                print("Finalizando...")
                sair = True
                
            sleep(7)
       except ValueError:
           print("Entrada inválida! Por favor, digite apenas números.")
       
