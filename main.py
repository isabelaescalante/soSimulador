#from simulador import SJF, SRT
class CPU:
    def __init__(self, i_d, tiempo_act):
        self.id = i_d
        self.tiempoact = tiempo_act
        self.tiempo_cc = 0

class Proceso:
    def __init__(self, i_d, at, et, io_flag, i_o=[]):
        self.id = i_d
        self.arr_time = at
        self.exe_time = et
        self.io_flag = io_flag
        self.io = i_o
        self.wait_time = 0
        self.end_time = 0
        self.cpuId = 0
    def add_CPU (self, actual, cant, arr_procesos):
        if actual >= cant :
            arr_procesos.sort(key=lambda x: (x.arr_time + x.exe_time), reverse=False)
            id_actual = arr_procesos[0].cpuId
            arr_procesos.pop(0)
            arr_procesos.append(self)
            self.cpuId = id_actual
        else :
            arr_procesos.append(self)
            self.cpuId = actual + 1
def get_CPU (arr_cpus):
        arr_cpus.sort(key=lambda x: (x.tiempoact), reverse=False)
        return arr_cpus[0]


def SJF(lista_procesos, context_switch, cpus) :
    print("SJF")
    #tiempo = 0
    #tiempo_cc = 0
    alguno = False
    actual = -1
    arr_cpus = []
    for x in range(0, cpus):
        arr_cpus.append(CPU(x,0))
    
    while len(lista_procesos) > 0 :
        for i in lista_procesos :
            alguno = False
            cpu = get_CPU(arr_cpus)
            if i.arr_time <= cpu.tiempoact :
                #i.add_CPU(actual, cpus, arr_procesos)
                #actual = actual + 1
                print("El proceso: " + str(i.id) + " esta en el CPU_" + str(cpu.id) + " , entro en el tiempo: " + str(cpu.tiempo_cc))
                if i.io_flag == 1 :
                    i.exe_time = i.exe_time - i.io[0]
                    cpu.tiempoact = cpu.tiempoact + i.io[0]
                    cpu.tiempo_cc = cpu.tiempoact
                    print("El proceso: " + str(i.id) + " se bloqueo en el tiempo " + str(cpu.tiempo_cc))
                    i.arr_time = cpu.tiempoact + i.io[1]
                    if len(i.io) > 2 :
                        i.io[2] = i.io[2] - i.io[0]
                        i.io.pop(0)
                        i.io.pop(0)
                        lista_procesos.sort(key=lambda x: (x.exe_time, x.arr_time, x.id), reverse=False)
                    else :
                        i.io_flag = 0
                else :
                    cpu.tiempoact = cpu.tiempo_cc
                    i.wait_time = cpu.tiempoact
                    i.end_time = i.wait_time + i.exe_time
                    cpu.tiempoact = cpu.tiempoact + i.exe_time
                    if len(lista_procesos) != 1 :
                        cpu.tiempo_cc = cpu.tiempoact + context_switch
                        print("El proceso: " + str(i.id) + " ha salido del CPU_" + str(cpu.id) + " en el tiempo " + str(cpu.tiempoact))
                    else:
                        print("El proceso: " + str(i.id) + " ha salido del CPU_" + str(cpu.id) + " en el tiempo " + str(cpu.tiempoact))
                    lista_procesos.remove(i)
                break
            else :
                for y in lista_procesos :
                    if y.arr_time <= cpu.tiempoact :
                        alguno = True
                        i = y
                        break
                if alguno == False :
                    lista_procesos.sort(key=lambda x: (x.arr_time, x.exe_time, x.id), reverse=False)
                    cpu.tiempoact = lista_procesos[0].arr_time
                    cpu.tiempo_cc = cpu.tiempoact
                    lista_procesos.sort(key=lambda x: (x.exe_time, x.arr_time, x.id), reverse=False)

def SRT(lista_procesos, context_switch, cpus) :
    print("SRT")
    tiempo = 0
    tiempo_cc = 0
    alguno = False 
    # remaining time del proceso dentro del CPU
    rtProceso = 10000000 
    while len(lista_procesos) > 0 :
        for i in lista_procesos :
            alguno = False
            if i.arr_time <= tiempo and i.exe_time < rtProceso :
                print("El proceso: " + str(i.id) + " esta en el cpu, entro en el tiempo: " + str(tiempo))
                if i.io_flag == 1 :
                    i.exe_time = i.exe_time - i.io[0]
                    tiempo = tiempo + i.io[0]
                    tiempo_cc = tiempo
                    print("El proceso: " + str(i.id) + " se bloqueo en el tiempo " + str(tiempo))
                    i.arr_time = tiempo + i.io[1]
                    if len(i.io) > 2 :
                        i.io[2] = i.io[2] - i.io[0]
                        i.io.pop(0)
                        i.io.pop(0)
                        lista_procesos.sort(key=lambda x: (x.exe_time, x.arr_time, x.id), reverse=False)
                    else :
                        i.io_flag = 0
                else :
                    tiempo = tiempo_cc
                    i.wait_time = tiempo
                    # i.end_time = i.wait_time + i.exe_time
                    tiempo = tiempo + 1
                    i.exe_time = i.exe_time -1
                    rtProceso = i.exe_time

                    if len(lista_procesos) == 1 :
                        print("El proceso: " + str(i.id) + " ha salido del cpu en el tiempo " + str(tiempo))
                    if i.exe_time == 0 :
                        lista_procesos.remove(i)
                    break

                    # if len(lista_procesos) != 1 :
                    #     tiempo_cc = tiempo + context_switch
                    #     print("El proceso: " + str(i.id) + " ha salido del cpu en el tiempo " + str(tiempo_cc))
                    # else:
                    #     print("El proceso: " + str(i.id) + " ha salido del cpu en el tiempo " + str(tiempo))
            else :
                for y in lista_procesos :
                    if y.arr_time <= tiempo :
                        alguno = True
                        break
                if alguno == False :
                    lista_procesos.sort(key=lambda x: (x.arr_time, x.exe_time, x.id), reverse=False)
                    tiempo = lista_procesos[0].arr_time
                    tiempo_cc = tiempo
                    lista_procesos.sort(key=lambda x: (x.exe_time, x.arr_time, x.id), reverse=False)
            

def leerArchivo() :
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
            elif words[0] == "QUANTUM" :
                quantum = int(words[1])
            elif words[0] == "CONTEXT" and words[1] == "SWITCH":
                context_switch =  int(words[2])
            elif words[0] == "CPUS" :
                cpus = int(words[1])
                # falta romper todo
            elif words[0].isdigit() :
                if len(words) == 3 :
                    error_proceso = True
                    proceso = Proceso(int(words[0]), int(words[1]), int(words[2]), 0)
                    lista_procesos.append(proceso)
                if len(words) > 3 :
                    if words[3] == "I/O" and ((len(words) - 4) % 2 == 0):
                        error_proceso = True
                        for i in words[4:] :
                            io.append(int(i))
                        proceso = Proceso(int(words[0]), int(words[1]), int(words[2]), 1, io)
                        lista_procesos.append(proceso)
                if not error_proceso :
                    print("El proceso: " + words[0] + " no se encuentra en el formato deseado")
                
                error_proceso = False
            elif words[0] == "FIN" :
                if politica == "-1" or quantum <> 0 or context_switch == -1 or cpus == 0 : 
                    flag = False
                else :
                    flag = True

    if flag :
        lista_procesos.sort(key=lambda x: (x.exe_time, x.arr_time, x.id), reverse=False)
        if politica == "SJF" :
            SJF(lista_procesos, context_switch, cpus)
        else :
            SRT(lista_procesos, context_switch, cpus)
        #for i in lista_procesos :
        #   print(i.id, i.arr_time, i.exe_time)
    else :
        print("Alguien eveneno el abrebadero")

if __name__ == "__main__":
    leerArchivo()