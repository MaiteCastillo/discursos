import os

#La comanda os.listdir ens llegeix tots els arxius que estan a la carpeta 
fitxers = os.listdir('discursos/')
for nomFitxer in fitxers:
    #nomFitxer conté el nom de l'arxiu que està en el directori 
    #s'obre per lectura
    fitxer = open('discursos/'+nomFitxer,"r")
   #Heu de posar la condició si està ben format o no 
    print("L'arxiu "+nomFitxer+" net queda")
   # Aquí heu pintar el text netejat
   
