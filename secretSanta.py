import random
import pandas as pd 
import numpy as np

givers = []
def dataFormatChoice():       #function to select data format. Can also use excel format additionally with few changes
    print("Hi!! To create Secret Santa gift pairs, select the data format you have")
    print("Press 1 if you have a csv file")
    print("Press 2 if you wish to enter names manually here")

    choice = int(input())
    if choice == 1:
        df = pd.read_csv("E:/secret santa/names.csv",usecols = [0])  # can enter the path of file that containers the Names of members
        givers = df['Names'].tolist() 
    else :
        givers = [str(x) for x in input("Enter the names of members ( separate names by comma) ").split(",")] 

    #print(givers)
    genSecretSanta(givers)

def genSecretSanta(givers):
    
    result = []
    restart = True

    while restart:
        restart = False
        receivers = givers[:]    #making a list same as givers

        for i in range(len(givers)):
            giver = givers[i]
            receiver = random.choice(receivers)   #randomly selecting a person from receivers
            if (giver == receiver and i == (len(givers) - 1)):
                restart = True
                break
            else:
                while (receiver == giver):            #checking if giver and receiver are different . if not choose again.
                    receiver = random.choice(receivers)
                result.append(giver + ' -----> '+ receiver)
                receivers.remove(receiver)            #once receiver is fixed , we can remove from the list
                
    for r in result:
        print(r)

def main():
    dataFormatChoice()    
    

if __name__ == '__main__':
    main()
