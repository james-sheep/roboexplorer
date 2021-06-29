import paho.mqtt.client as mqtt
from classRobot import *
from time import sleep


pinochio = Robot(14, 12, 7)

def on_connect(client, userdata, flags, rc):

    client.subscribe("robot_mensagem")
    client.subscribe("robot_garraH")
    client.subscribe("robot_marcha")
    client.subscribe("robot_seguir")
    client.subscribe("robot_L")
    client.subscribe("robot_R")
    

def on_message(client, userdata, msg):
    
    texto1 = str(msg.payload)
    texto_tratado = texto1.strip("b")
   
    if texto_tratado =='22d47bba.1b228c': # Frente
        
        pinochio.movienta_frente()
        
        
    elif texto_tratado =='8b28ae10.e9829':    # Trás
        
        pinochio.movienta_tras()
        
        
    elif texto_tratado =='bfb7ed36.494608':  # Esquerda
        
         pinochio.movienta_esquerda()
        
    elif texto_tratado =='e6f04e5b.e79338':   # Direita
      
       pinochio.movienta_direita()
      
      
    elif texto_tratado =='17dcc6b7.fcac51': # Abre Garra
   
       pinochio.movienta_garra_abre()
      
      
    elif texto_tratado =='50df1441.87c1ac': # Fecha Garra
    
        pinochio.movienta_garra_fecha()
    
    else:
         print(texto_tratado)
  
client = mqtt.Client()
client.connect("192.168.0.42", 1883)

client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()

