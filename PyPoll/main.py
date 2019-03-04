'''
Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
'''


import csv
import os

filepath= "election_data.csv"

Totvotes = 0
Khanvote =0
Correyvote =0
Livote=0
OToolvote=0

with open(filepath) as elect:
    fileread = csv.reader(elect, delimiter=',')
    csvheader = next(fileread)

    for row in fileread:
        Totvotes = Totvotes + 1

        if row[2] == "Khan":
            Khanvote= Khanvote+1
        elif row[2] == "Correy":
            Correyvote = Correyvote+1
        elif row[2] == "Li":
            Livote= Livote+1
        elif row[2] == "O'Tooley":
            OToolvote = OToolvote +1

    
Candidates= {'Khan': Khanvote, 'Correy': Correyvote, 'Li': Livote, 'O\'Tooley':OToolvote}

print("Election Results")
print("--------------------------")
print(f'Total Votes: {Totvotes}')
print("--------------------------")
print(f'Khan {format(Khanvote/Totvotes*100, ".3f")}% ({Khanvote})')
print(f'Correy {format(Correyvote/Totvotes*100, ".3f")}% ({Correyvote})')
print(f'Li {format(Livote/Totvotes*100, ".3f")}% ({Livote})')
print(f'O\'Tooley {format(OToolvote/Totvotes*100, ".3f")}% ({OToolvote})')
print("--------------------------")
print(f'Winner is {max(Candidates, key=Candidates.get)}')
print("--------------------------")

myfile=open("ElectionWinners.txt", "w+") 
    
myfile.write("Election Results" '\n')    
myfile.write("--------------------------" '\n')
myfile.write(f'Total Votes: {Totvotes} \n')   
myfile.write("--------------------------" '\n')
myfile.write(f'Khan {format(Khanvote/Totvotes*100, ".3f")}% ({Khanvote}) \n')    
myfile.write(f'Correy {format(Correyvote/Totvotes*100, ".3f")}% ({Correyvote}) \n')
myfile.write(f'Li {format(Livote/Totvotes*100, ".3f")}% ({Livote}) \n') 
myfile.write(f'O\'Tooley {format(OToolvote/Totvotes*100, ".3f")}% ({OToolvote}) \n') 
myfile.write("--------------------------" '\n') 
myfile.write(f'Winner is {max(Candidates, key=Candidates.get)} \n') 
myfile.write("--------------------------" '\n') 