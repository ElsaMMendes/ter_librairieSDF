#!/usr/bin/python
# -*-coding:Utf-8 -*


import os,sys
nb = sys.argv[-1]



pathinput = "C:\\Users\\MENDES\\Downloads\\UNIV\\L3\\S5\\TER\\TERibcp\\librairie_SDF\\data\\"
pathoutput = "C:\\Users\\MENDES\\Downloads\\UNIV\\L3\\S5\\TER\\TERibcp\\librairie_SDF\\data\\"
max_file = 4
inputfile = "test.sdf" 
cpt = 1
cptfile = 0

outputfile = open("%s/%s_%03d.sdf"%(pathoutput,inputfile[:-4],cpt),"w")

with open("%s/%s"%(pathinput,inputfile),"r") as infile:
    while 1:
        line = infile.readline()
        if line:
            if line.find("$$$$") != -1:
                cptfile += 1
                outputfile.write(line)
            else:
                outputfile.write(line)
            if cptfile == max_file:
                outputfile.close
                cpt += 1
                cptfile = 0
                outputfile = open("%s/%s_%03d.sdf"%(pathoutput,inputfile[:-4],cpt),"w")
        else:
            break

infile.close()
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


