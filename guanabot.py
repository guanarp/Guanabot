import discord
import time
import datetime
from discord.ext import commands,tasks
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
channel = os.getenv('CHANNEL')


client=commands.Bot(command_prefix='.')

class Materia:
    def __init__(self, nombre, dia, horas, mins,link="NN",sgteExamen=0):
        self.dia=dia
        self.nombre=nombre
        self.horas=horas
        self.mins=mins
        self.link=link
        self.sgteExamen=sgteExamen
    
    def getNombre(self):
        return self.nombre
    def setNombre(self,arg):
        self.nombre =arg

    def getDia(self):
        return self.dia
    def setDia(self,arg):
        self.dia =arg

    def getHoras(self):
        return self.horas
    def setHoras(self,arg):
        self.horas =arg  

    def getMins(self):
        return self.mins
    def setMins(self,arg):
        self.mins =arg

    def getLink(self):
        return self.link
    def setLink(self,arg):
        self.link =arg

    def getSgteExamen(self):
        return self.sgteExamen
    def setSgteExamen(self,arg):
        self.sgteExamen =arg              

#aki le agregas el  
# li    
# def nk como string nomas a cada uno al final
poo=Materia('POO',1,14,0,'https://meet.google.com/aek-behh-hkr',datetime.datetime(2020,8,31))
fs_practica=Materia('FS Practica',2,7,30,'https://meet.google.com/gri-gvoy-gip')
dinamica=Materia('Dinamica Charly',2,9,0)
teoriaDeCircuitos=Materia('Teoria de Circuitos',2,16,0,'https://meet.google.com/lookup/akks57i7ph',datetime.datetime(2020,9,8))
mn=Materia('MN Practica',3,13,0,'https://meet.google.com/lookup/e5fl37ajgl')
dinamicaP=Materia('Dinamica Practica C',4,8,0,'https://meet.google.com/lookup/bgk5osrwbj',datetime.datetime(2020,8,27))
tc=Materia('TC Practica',4,16,0,'https://meet.google.com/lookup/akks57i7ph')
fs_teoria=Materia('FS Teoria',4,18,0,'https://meet.google.com/gri-gvoy-gip',datetime.datetime(2020,8,24))
mnt=Materia('MN Teoria',5,8,30,'https://meet.google.com/lookup/e5fl37ajgl',datetime.datetime(2020,9,5))

materias=[poo,fs_practica,dinamica,teoriaDeCircuitos,mn,dinamicaP,tc,fs_teoria,mnt]
materias.append(Materia("Materia de prueba de lunes",0,23,21,"https://twitter.com/josecarios",datetime.datetime(2020,8,24,22,10)))


@client.event
async def on_ready():
    print('Yasta el bot')
    hora.start()

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency* 1000)}ms')

@tasks.loop(seconds=60)
async def hora():
    #channel=client.get_channel("") #aca tenes que poner el channel ID del canal al que queres enviar el mensaje
    channel2 = client.get_channel(int(channel))
    for x in materias:
        horario = time.localtime(time.time())
        hora = x.getHoras()
        #print(hora)
        mins = x.getMins()
        if (hora - 30)<0:
            hora30 = hora-1
            mins30 = (mins-30)%60
        else:
            hora30 =hora
            mins30 = mins-30
        if (hora - 5)<0:
            hora5 = hora-1
            mins5 = (mins-5)%60
        else:
            hora5=hora
            mins5= mins-5
        print(horario)
        if(horario.tm_wday==x.getDia() and horario.tm_hour==x.getHoras() and horario.tm_min==x.getMins()):
            print("OK")
            #await channel.send(f"@everyone  Es hora de la clase de {x.getNombre()} beep boop, el link es {x.getLink()}")
            await channel2.send(f"Es hora de la clase de {x.getNombre()} beep boop, el link es {x.getLink()}")
        if(horario.tm_wday==x.getDia() and horario.tm_hour==hora30 and horario.tm_min== mins30):
            print("OK")
            #await channel.send(f"La clase de {x.getNombre()} comienza en 30 mins beep boop")
            await channel2.send(f"La clase de {x.getNombre()} comienza en 30 mins beep boop")
        if(horario.tm_wday==x.getDia() and horario.tm_hour==hora5 and horario.tm_min==mins5 ):
            print("OK")
            #await channel.send(f"La clase de {x.getNombre()} comienza en 5 mins beep boop")
            await channel2.send(f"La clase de {x.getNombre()} comienza en 5 mins beep boop")
        fechaD = x.getSgteExamen()
        print(fechaD)
        fechahoy = datetime.datetime(2020,horario.tm_mon,horario.tm_mday)
        print(fechahoy)
        try:
            print( fechaD-fechahoy )
            if(fechaD-fechahoy== datetime.timedelta(days=7) and horario.tm_hour==22 and horario.tm_min==44):
                await channel2.send(f"El examen de {x.getNombre()} es en 5 dias beep boop")
            if(fechaD-fechahoy== datetime.timedelta(days=3) and horario.tm_hour==12 and horario.tm_min==0):
                await channel2.send(f"El examen de {x.getNombre()} es en 3 dias beep boop")
            if(fechaD-fechahoy== datetime.timedelta(days=1) and horario.tm_hour==12 and horario.tm_min==0):
                await channel2.send(f"El examen de {x.getNombre()} es manhana beep boop")
        except TypeError:
            continue








client.run(TOKEN)
