#rosco1=open("D:\\Users\\Usuario\\Documents\\prueba\\Definiciones1.txt")
#linea=rosco1.readline()
abecedario=["A ","B ","C ","D ","E ","F ","G ","H ","I ","J ","K ","L ","M ","N ","O ","P ","Q ","R ","S ","T ","U ","V ","W ","X ","Y ","Z "]
j=0
aciertos=0
errores=0
sinRespuesta=26
for j in range(3):
    rosco1=open("D:\\Users\\Usuario\\Documents\\prueba\\Definiciones1.txt")
    linea=rosco1.readline()
    for j in range (26): 
        #for i in range(26):
            #print(abecedario[i],end=" ")
        #i=0
        #print()

        campos=linea.strip().split(":")
        if (abecedario[j]!="🟩" and abecedario[j]!="🟥"):
            for i in range(26):
                print(abecedario[i],end=" ")
            i=0
            print()
    #if(campos!="🟩" or "🟥"):
            print(campos[0])
            print(campos[1])
            respuesta=input("Respuesta:")
            respuesta=respuesta.upper()
            if(respuesta==campos[2]):
            #campos[0]="🟩"
                abecedario[j]="🟩"
                aciertos=aciertos+1
                sinRespuesta=sinRespuesta-1
        
            #for i in range(26):
             #   print(abecedario[i],end=" ")

            elif(respuesta=="PASAPALABRA"):
                print()
                #sinRespuesta=sinRespuesta+1
        #elif(respuesta!="PASAPALABRA" or campos[2]):
            else:
                abecedario[j]="🟥"
                errores=errores+1
                sinRespuesta=sinRespuesta-1
            linea=rosco1.readline()
        else:
            linea = rosco1.readline()
        j+=1
    j=0
j=0
i=0
for i in range(26):
    print(abecedario[i],end=" ")
print()
print("ACIERTOS: ",aciertos,"\n","ERRORES: ",errores,"\n","PASAPALABRAS: ",sinRespuesta)
rosco1.close()
