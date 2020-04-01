from numaleatorios import Aleatorio
import math
import statistics

random  = Aleatorio()

class Evento():

    def __init__(self):
        super().__init__()
        self.tipo_evento = ""
        self.tiempo_creacion = 0
        self.tiempo_salida = 0
        
#Simulacion en minutos

## Creacion de llegadas
tiempo = 0
# SIMULACION POR 80 HORAS, EN MINUTOS = 4800
tiempo_max = 4800
# LISTA DONDE SE VAN A GUARDAR TODOS LOS EVENTOS
eventos = []
# CICLO PARA LAS LLEGADAS DE LOS CLIENTES RAPIDOS
while(tiempo < tiempo_max):
    evento = Evento()
    tiempo = tiempo + random.exponencial(8) #TIEMPO DE LLEGADA EXPONENCIAL CON MEDIA DE 8 MINUTOS
    evento.tiempo_creacion = tiempo 
    evento.tiempo_evento = evento.tiempo_creacion
    evento.tipo_evento = "llegada_rapida"
    eventos.append(evento)

tiempo = 0
    
# CICLO PARA LAS LLEGADAS DE LOS CLIENTES LENTOS
while(tiempo < tiempo_max):
    evento = Evento()
    tiempo = tiempo + random.exponencial(20) #TIEMPO DE LLEGADA EXPONENCIAL CON MEDIA DE 20 MINUTOS
    evento.tiempo_creacion = tiempo 
    evento.tiempo_evento = evento.tiempo_creacion
    evento.tipo_evento = "llegada_lenta"
    eventos.append(evento)
    
tiempo = 0    
# CICLO PARA EL ESCANER
while(tiempo < tiempo_max):
    evento = Evento()
    tiempo = tiempo + 1 #AGREGAMOS 1 MINUTO A EL ESCANER PARA CHECAR CADA 1 MINUTO
    evento.tiempo_creacion = tiempo 
    evento.tiempo_evento = evento.tiempo_creacion
    evento.tipo_evento = "escaner"
    eventos.append(evento)

## Inicio de la simulacion 
tiempo = 0
cola_de_espera_Rapida = []
cola_de_espera_Lenta = []
salidas = []
cajera_caja_rapida_ocupada = False
cajera_caja_lenta_ocupada = False
listaClientesEnColaDeEsperaRapida = []
listaClientesEnColaDeEsperaLenta = []
# piezas_max = 0

# SIMULACIÓN PARA LA CAJA RÁPIDA
while(tiempo < tiempo_max):
    eventos.sort(key=lambda x:x.tiempo_evento)
    evento = eventos.pop(0) ## Evento proximo
    tiempo = evento.tiempo_evento
    
    if(evento.tipo_evento=="escaner"):
        listaClientesEnColaDeEsperaRapida.append(len(cola_de_espera_Rapida))
        listaClientesEnColaDeEsperaLenta.append(len(cola_de_espera_Lenta))
    
    if(evento.tipo_evento == "llegada_rapida"):
        if(len(cola_de_espera_Rapida) == 0 and cajera_caja_rapida_ocupada == False):
            cajera_caja_rapida_ocupada = True
            evento.tiempo_inspeccion = tiempo
            evento.tiempo_evento = tiempo + random.exponencial(2) ##TIEMPO EN QUE ATIENDEN EN LA CAJA RÁPIDA
            evento.prevEvento = evento.tipo_evento
            evento.tipo_evento ="salida_atendido_rapido"
            evento.tiempo_salida_rapido = evento.tiempo_evento
            eventos.append(evento)
            #AGREGAR QUE HAY 0 PERSONAS EN LA COLA
            # listaClientesEnColaDeEsperaRapida.append(len(cola_de_espera_Rapida))
        else:
            cola_de_espera_Rapida.append(evento)
            # listaClientesEnColaDeEsperaRapida.append(len(cola_de_espera_Rapida)) #AQUI SE AGREGA A UNA LISTA LA CANTIDAD DE CLIENTES EN LA COLA DE ESPERA
    
            
                      
            
    elif( evento.tipo_evento == "salida_atendido_rapido"):
        cajera_caja_rapida_ocupada = False
        evento.tiempo_salida_rapido = tiempo
        salidas.append(evento)
        if(len(cola_de_espera_Rapida)>0):
            pieza = cola_de_espera_Rapida.pop(0)
            cajera_caja_rapida_ocupada = True
            pieza.tiempo_inspeccion = tiempo
            pieza.tiempo_evento = tiempo + random.exponencial(2) ##TIEMPO EN QUE ATIENDEN EN LA CAJA RAPIDA 
            pieza.tiempo_salida = pieza.tiempo_evento
            pieza.prevEvento = pieza.tipo_evento
            pieza.tipo_evento ="salida_atendido_rapido"
            eventos.append(pieza)
            # listaClientesEnColaDeEsperaRapida.append(len(cola_de_espera_Rapida)) #AQUI SE AGREGA A UNA LISTA LA CANTIDAD DE CLIENTES EN LA COLA DE ESPERA
            
    
            
    elif(evento.tipo_evento == "llegada_lenta"):
        if(len(cola_de_espera_Lenta) == 0 and cajera_caja_lenta_ocupada == False):
            cajera_caja_lenta_ocupada = True
            evento.tiempo_inspeccion = tiempo
            evento.tiempo_evento = tiempo + random.exponencial(16.4) ##TIEMPO EN QUE ATIENDEN EN LA CAJA RÁPIDA
            evento.prevEvento = evento.tipo_evento
            evento.tipo_evento ="salida_atendido_lento"
            evento.tiempo_salida_lento = evento.tiempo_evento
            eventos.append(evento)
            #AGREGAR QUE HAY 0 PERSONAS EN LA COLA
            # listaClientesEnColaDeEsperaLenta.append(len(cola_de_espera_Lenta))
        else:
            cola_de_espera_Lenta.append(evento)
            # listaClientesEnColaDeEsperaLenta.append(len(cola_de_espera_Lenta)) #AQUI SE AGREGA A UNA LISTA LA CANTIDAD DE CLIENTES EN LA COLA DE ESPERA
            
    elif( evento.tipo_evento == "salida_atendido_lento"):
        cajera_caja_lenta_ocupada = False
        evento.tiempo_salida_lento = tiempo
        salidas.append(evento)
        if(len(cola_de_espera_Lenta)>0):
            pieza = cola_de_espera_Lenta.pop(0)
            cajera_caja_lenta_ocupada = True
            pieza.tiempo_inspeccion = tiempo
            pieza.tiempo_evento = tiempo + random.exponencial(16.4) ##TIEMPO EN QUE ATIENDEN EN LA CAJA LENTA 
            pieza.tiempo_salida = pieza.tiempo_evento
            pieza.prevEvento = pieza.tipo_evento
            pieza.tipo_evento ="salida_atendido_lento"
            eventos.append(pieza)
            # listaClientesEnColaDeEsperaLenta.append(len(cola_de_espera_Lenta)) #AQUI SE AGREGA A UNA LISTA LA CANTIDAD DE CLIENTES EN LA COLA DE ESPERA
            



for x in listaClientesEnColaDeEsperaRapida:
    print ( x )
    
    
print("separacion")

for x in listaClientesEnColaDeEsperaLenta:
    print ( x )


def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
 
    return sum/len(lista)

promedio1 = promediarLista(listaClientesEnColaDeEsperaRapida)

promedio2 = promediarLista(listaClientesEnColaDeEsperaLenta)

# promedio1 = mean(listaClientesEnColaDeEsperaRapida)

print (promedio1)

print (promedio2)

print(statistics.mean(listaClientesEnColaDeEsperaRapida)) #Utilizando el método que me comentó el profe

print(statistics.mean(listaClientesEnColaDeEsperaLenta)) #Utilizando el método que me comentó el profe

# print ("F")

