#from simulador import SJF, SRT

politica = "-1"
quantum = -1
context_switch = -1
cpus = 0
procesoID = []
arrival_time = []
execution_time = []
io_dict = dict()
error_procesos = False

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
                procesoID.append(int(words[0]))
                arrival_time.append(int(words[1]))
                execution_time.append(int(words[2]))
            if len(words) > 3 :
                if words[3] != "I/O" :
                    error_procesos = True
        if words[0] == "FIN" :
            if politica == "-1" or quantum <> 0 or context_switch == -1 or cpus == 0 or error_procesos or len(procesoID) == 0  : 
                print "error"
            else :
                print "correct"




print politica
print quantum
print context_switch
print cpus
print procesoID
print arrival_time 
print execution_time
