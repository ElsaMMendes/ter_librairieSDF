#! /usr/bin/env python3
# -*-coding:Utf-8 -*

# code pour modifier les fichiers 
# ATTENTION : une idée de ce qui peut être fait mais LE CODE NE MARCHE PAS . PROBLEME AVEC PICKLE 

import os,sys
import pickle
nb = sys.argv[-1]

inputfile= "C:\\Users\\MENDES\\Downloads\\UNIV\\L3\\S5\\TER\\TERibcp\\librairie_SDF\\data\\test_003.sdf"


#variable à enregistrer 
var1 = [25]
var2 = ["deuxième ajout" , 5000]


#pour l'enregistrement d'objets dans un fichier 
with open(inputfile , 'ab') as fichier:   
    mon_pickler = pickle.Pickler(fichier)  #enregistrement 
    mon_pickler.dump(var1) 
    mon_pickler.dump(var2)  #entre parenthèses mettre l'élément à ajouter dans fichier et mettre cette ligne autant de fois que necessaire si plusieurs objets à enregistrer
fichier.close()


#récupérer objets enregistrés , restitution de la variable et son type 
with open(inputfile, 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier) # Lecture des objets contenus dans le fichier
    obj_recup_1 = mon_depickler.load()
    print(obj_recup_1, type(obj_recup_1))  
    obj_recup_2 = mon_depickler.load() 
    print(obj_recup_2, type(obj_recup_2)) 
fichier.close()




os.system("pause") 




def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__)) # we get the right path.
    path_to_file = os.path.join(directory, "data", data_file) # with this path, we go inside the folder `data` and get the file.

    try: 
         with open(path_to_file,"r") as f:
            preview = f.readline()
            print("Yeah! We managed to read the file. Here is a preview:")
            print(preview)
    except FileNotFoundError as e:
        print("Ow :( The file was not found. Here is the original message of the exception :", e)
    except:
        print('Destination unknown')
   