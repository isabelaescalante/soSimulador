#from simulador import SJF, SRT
class Proceso:
    def __init__(self, i_d, at, et, i_o=[]):
        self.id = i_d
        self.arr_time = at
        self.exe_time = et
        self.io = i_o
        self.wait_time = 0
        self.end_time = 0


politica = "-1"
quantum = -1
context_switch = -1
cpus = 0
error_procesos = False
lista_procesos = []


with open("cases.txt") as archivo_entrada :
    for line in archivo_entrada :
        words = line.split()
        if words[0] == "SJF" or words[0] == "SRT":
            politica = words[0]
        if words[0] == "QUANTUM" :
            quantum = int(words[1])
        if words[0] == "CONTEXT" :
            context_switch =  int(words[2])
        if words[0] == "CPUS" :
            cpus = int(words[1])
        if words[0].isdigit() :
            if len(words) < 3 :
                error_procesos = True
            if len(words) == 3 :
                if words[2] == 0 :
                    error_procesos = True
                else :
                    proceso = Proceso(int(words[0]), int(words[1]), int(words[2]))
                    lista_procesos.append(proceso)
            if len(words) > 3 :
                if words[3] != "I/O" :
                    error_procesos = True
                    proceso = Proceso(int(words[0]), int(words[1]), int(words[2]))
                    lista_procesos.append(proceso)
        if words[0] == "FIN" :
            if politica == "-1" or quantum <> 0 or context_switch == -1 or cpus == 0 or error_procesos or len(lista_procesos) == 0  : 
                print "error"
            else :
                print "correct"
            
            #imprime input
            print politica
            print quantum
            print context_switch
            print cpus
            print procesoID
            print arrival_time 
            print execution_time

            #inicia los valores otra vez para siguiente simulación
            politica = "-1"
            quantum = -1
            context_switch = -1
            cpus = 0
            error_procesos = False
            lista_procesos = []