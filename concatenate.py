#!/usr/bin/python
# -*-coding:Utf-8 -*

import os,sys 

filenames = ["C:\\Users\\MENDES\\Downloads\\UNIV\\L3\\S5\\TER\\TERibcp\\librairie_SDF\\data\\test_001.sdf", 
"C:\\Users\\MENDES\\Downloads\\UNIV\\L3\\S5\\TER\\TERibcp\\librairie_SDF\\data\\test_002.sdf",
"C:\\Users\\MENDES\\Downloads\\UNIV\\L3\\S5\\TER\\TERibcp\\librairie_SDF\\data\\test_003.sdf"]

pathoutput = "C:\\Users\\MENDES\\Downloads\\UNIV\\L3\\S5\\TER\\TERibcp\\librairie_SDF\\data\\"
output = pathoutput  + "_regroupement.sdf"
cptfile = 0

outputfile = open(output,"w")

for fnames in filenames:
    with open (fnames, "r") as f:
        while 1:
            line= f.readline()
            if line:
                if line.find("$$$$") != -1:
                    cptfile += 1
                    outputfile.write(line)
                else:
                    outputfile.write(line)
            else:
                break
                 
    f.close()

outputfile.close()


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
   

os.system("pause")



