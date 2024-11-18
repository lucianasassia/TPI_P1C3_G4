rosco1=open("D:\\Users\\Usuario\\Documents\\prueba\\Definiciones1.txt")
linea=rosco1.readline()
abecedario=["A ","B ","C ","D ","E ","F ","G ","H ","I ","J ","K ","L ","M ","N ","O ","P ","Q ","R ","S ","T ","U ","V ","W ","X ","Y ","Z "]
j=0
while (linea):

    for i in range(26):
        print(abecedario[i],end=" ")
    i=0
    print()
    campos=linea.strip().split(":")
            #for i in range(26):
    if(campos[0]!="🟩" or campos[0]!="🟥"):
        print(campos[0])
        print(campos[1])
        respuesta=input("Respuesta:")
        respuesta=respuesta.upper()
        if(respuesta==campos[2]):
            campos[0]="hecho"
             #   print(abecedario[i],end=" ")

        elif(respuesta=="PASAPALABRA"):
            print()
        elif(respuesta!="PASAPALABRA" or campos[2]):
             campos[0]="hecho"
             abecedario[j]="🟥"
        linea=rosco1.readline()
    j+=1
