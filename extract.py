#!/usr/bin/python
# -*-coding:Utf-8 -*

#pour extraire diverses informations sur un fichier en particulier 

import os,sys 
nb = sys.argv[-1]

inputfile= "C:\\Users\\MENDES\\Downloads\\UNIV\\L3\\S5\\TER\\TERibcp\\librairie_SDF\\data\\test_003.sdf"
counter = 0

 
print("tapez '1' si vous voulez une lecture du fichier inputfile ligne par ligne")
print("tapez '2' si vous voulez une lecture du fichier pour une ligne voulue")
print("tapez '3' si vous voulez savoir le nombre de molécules du fichier ")
choix = input()


if choix == "1" :
    with open(inputfile) as f:
	    for line in f:
		    print ("=>"+line)
    f.close()

elif choix == "2" : 
    with open(inputfile,'r') as f:
        for i in range(10):
            line = f.readline()
            print(i,line) 
    f.close()

elif choix == "3": 
    with open(inputfile,"r") as f:
        while 1:
            line = f.readline()
            if line: 
                if line.find("<Hf>") != -1 :
                    counter += 1
                    print(counter ,"molécule(s) trouvée(s)")
    f.close()
else :
    print ("un nombre entre 1 et 3 svp")

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
   


