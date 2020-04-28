import os

#La comanda os.listdir ens llegeix tots els arxius que estan a la carpeta 
fitxers = os.listdir('poesia/')
for nomFitxer in fitxers:
    #nomFitxer conté el nom de l'arxiu que està en el directori 
    #s'obre per lectura
    fitxer = open('poesia/'+nomFitxer,"r")
   #Heu de posar la condició si està ben format o no 
    print("La poesia "+nomFitxer)
   # Aquí heu pintar quin tipus de rima té
