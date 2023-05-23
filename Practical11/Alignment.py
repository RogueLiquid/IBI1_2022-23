#First the protein sequences should be readed
#Then for 2 sequences, every amino acid od the same place should be compared
#the result of comparison will be scored and added, percentage will be calculated
#Showing the result
#import os
#print(os.getcwd())
#os.chdir("D:/college/first year/IBI1/practical/11")
#print(os.getcwd()
import openpyxl
human = open("ACE2_human.fa","r")
cat = open("ACE2_cat.fa","r")
mouse = open("ACE2_mouse.fa","r")
blosum = openpyxl.load_workbook("BLOSUM.xlsx")
worksheet = blosum["Sheet1"]

def rd(file):
    filetext = []
    for line in file:
        if not line.startswith(">"):
            line = line.strip()
            filetext.append(line)
    return filetext[0]

def cp(file1,file2):
    score = 0
    count = 0
    tr = True
    for row in worksheet.values:
       if tr == True:
           row1 = row
           tr = False
    for i in range(0,len(file1)):
        if file1[i] == file2[i]:
             count += 1
        for row in worksheet.values:
            if row[0] == file1[i]:
                for k in range(0,24):
                    if row1[k] == file2[i]:
                        score = score + row[k]
    percentage = count/len(file1)*100
    
    print("the score is " + str(score))
    print("the percentage is " + str(percentage) + "%")

cattxt = rd(cat)
mousetxt = rd(mouse)
humantxt = rd(human)

print("for mouse and cat ")
cp(mousetxt,cattxt)

print("for mouse and human ")
cp(mousetxt,humantxt)

print("for human and cat ")
cp(humantxt,cattxt)