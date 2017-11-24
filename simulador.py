#imprime el tiempo, la cola de listas, cpu y procesos bloqueados cuando hay cambios durante la simulación
def printChanges() :
    print "Tiempo\tCola de listas\t",
    for i in range(1,cpus+1) :
        print "\tCPU" + str(i) + "\t" ,
    print "Procesos bloqueados"

    print processID,"\t\t",2,"\t\t",str(20),"\t\t",str(8),"\t\t",str(5)

#imprime los tiempos de turnaround y espera de los procesos con su promedio al final de la simulación
def printFinal() :
    turnarounds = [4,2]
    espera = [3,5]
    promedioTurnaround = 0
    promedioEspera = 0
    proceso = 2 
    print "Proceso\t\tTiempo de turnaround\tTiempo de espera"
    for x in range(1,proceso+1) :
        print str(x),"\t\t\t",str(turnarounds[x-1]),"\t\t\t",str(espera[x-1])

    print "Promedio de turnaround: ",
    print (sum(turnarounds) / proceso)
    print "Promedio de espera: ",
    print (sum(espera) / proceso)

#def SRT() :


#def SJF() :


printFinal()