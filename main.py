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
flag = False
lista_procesos = []
io = []
error_proceso = False

with open("cases.txt") as archivo_entrada :
    for line in archivo_entrada :
        words = line.split()
        if words[0] == "SJF" or words[0] == "SRT":
            politica = words[0]
        if words[0] == "QUANTUM" :
            quantum = int(words[1])
        if words[0] == "CONTEXT" and words[1] == "SWITCH":
            context_switch =  int(words[2])
        if words[0] == "CPUS" :
            cpus = int(words[1])
            # falta romper todo
        if words[0].isdigit() :
            if len(words) == 3 :
                error_proceso = True
                proceso = Proceso(int(words[0]), int(words[1]), int(words[2]))
                lista_procesos.append(proceso)
            if len(words) > 3 :
                if words[3] == "I/O" and ((len(words) - 4) % 2 == 0):
                    error_proceso = True
                    for i in words[4:] :
                        io.append(int(i))
                    proceso = Proceso(int(words[0]), int(words[1]), int(words[2]), io)
                    lista_procesos.append(proceso)
            if not error_proceso :
                print("El proceso: " + words[0] + " no se encuentra en el formato deseado")
            
            error_proceso = False
        if words[0] == "FIN" :
            if politica == "-1" or quantum <> 0 or context_switch == -1 or cpus == 0 : 
                flag = False
            else :
                flag = True

if flag :
    lista_procesos.sort(key=lambda x: (x.arr_time, x.exe_time), reverse=False)
    #for i in lista_procesos :
    #   print(i.id, i.arr_time, i.exe_time)