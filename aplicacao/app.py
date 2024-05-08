import requests
from time import sleep
import os
class App:
    
    def __init__(self):
        
            
            self.HOST = "http://"+ os.getenv('SERVER-IP') +":59998"
            self.BUFFER_SIZE = 2048
     
    def alterar_temp_amostragem(self, segundos, matricula):
        url = f'{self.HOST}/alterar_temp_amostragem/{segundos}/{matricula}'  # URL do servidor
        
        response = requests.get(url)
        print(response.json())

    def enviar_comando(self, comando, matricula):
        url = f'{self.HOST}/enviar_comando/{comando}/{matricula}'  # URL do servidor
        
        response = requests.get(url)
        print(response.json())
        
    def pedir_medicao(self,matricula):
        url = f'{self.HOST}/receber_medicao/{matricula}'  # URL do servidor
        
        response = requests.get(url)
        print(response.json())

    #Prints para o MENU
def exibir_opcoes():
    print("\n===== Bem-vindo ao Menu =====\n")
    print("1. Solicitar dados de um sensor:")
    print("2. Enviar comando para um sensor Ligar ou Desligar")
    print("3. Alterar tempo de amostragem ")
    print("4. Sair")
   
# Verifica se um número foi digitado ou não
def verificar_numero(numero):
    
    try:
        numero = int(numero)
        return True
    
    except:
         return False

#Loop principal
if __name__ == '__main__':
    app = App()
    
    
    while(True):
       exibir_opcoes()
       
       try:
            entrada = input("Digite um número:\n")
            numero = int(entrada)
            
            
            if(numero > 5 or numero <= 0):
                
                    print("Entrada inválida! Por favor, digite um número válido.")
        
            
            elif(numero == 1):
                
                os.system('clear')
                matricula = input("Digite a matricula do sensor que deseja solicitar os dados:\n")
                
                
                if(verificar_numero(matricula)):
                    app.pedir_medicao(matricula)
                else:
                    print("Entrada inválida! Por favor, digite um número válido.")
            
            elif(numero == 2):
                
                os.system('clear')
                matricula = input("Digite a matricula do sensor que deseja enviar o comando:\n")
                
                if(verificar_numero(matricula)):
                    comando = input("Digite o comando 'Ligar' ou 'Desligar'\n")
                    comando = comando.lower()
                    if(comando == "ligar" or comando == "desligar"):
                        app.enviar_comando(comando, matricula)
                    else:
                        print(f"Comando '{comando}' não reconhecido!")
                        
                else:print(f"Matricula digitada '{matricula}' não reconhecida!")
                    
            elif(numero == 3):
                
                os.system('clear')
                matricula = input("Digite a matricula do sensor que deseja alterar o tempo de amostragem:\n")
                
                if(verificar_numero(matricula)):
                   segundos = input("Digite o intervalo de envio em segundos:\n")
                   
                   if(verificar_numero(segundos)):
                       
                        app.alterar_temp_amostragem(segundos, matricula)
                        
                   else: 
                       print(f"Tempo digitado '{segundos}' não reconhecido!")
                   
                else:
                    print(f"Matricula digitada '{matricula}' não reconhecida!")
                          
            elif(numero == 4):
                print("Finalizando...")
                
       except ValueError:
           print("Entrada inválida! Por favor, digite apenas números.")
    
           
    
