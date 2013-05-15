def writenote(student, filelist):
    filename = student + ".txt"
    outpath = os.getenv("Home") + "Useagenotes\\" + filename
    fileout = open (outpath, "wt")
    fileout.write('''
Please investigate the following files which are on your home drive.\n
if these files are not for school work purposes please delete them. \n\n
if they are for school work purposes please speak to Mr Jones\n\n
''')
    for file in filelist:
        fileout.write(file[3:])
        fileout.write ("\n")
    fileout.close()

import os
startPath = "U:"
students = os.listdir(startPath)
susList = ['exe','bat','avi','wmv','mp4']
studentlist = open('studentlist.txt', "w")
for student in students:
    filelist = []
    path = startPath + "\\" + student
    for triple in os.walk(path):
        for file in triple[2]:
            dot = file.find(".")
            extension = file[dot+1:]
            if (extension in susList)and (file[0]!='$'):
                filelist.append(triple[0] +'\\' +file)
    if len(filelist)>0:
        studentlist.write(student +"\n")
        writenote(student,filelist)
studentlist.close()    
