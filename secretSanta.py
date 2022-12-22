import random
import pandas as pd 
import numpy as np

givers = []
def dataFormatChoice():
    print("Hi!! To create Secret Santa gift pairs, select the data format you have")
    print("Press 1 if you have a csv file")
    print("Press 2 if you wish to enter names manually here")

    choice = int(input())
    if choice == 1:
        df = pd.read_csv("E:/secret santa/names.csv",usecols = [0])
        givers = df['Names'].tolist() 
    else :
        givers = [str(x) for x in input("Enter the names of members ( separate names by comma) ").split(",")] 

    print(givers)
    genSecretSanta(givers)

def genSecretSanta(givers):
    
    result = []
    restart = True

    while restart:
        restart = False
        receivers = givers[:]

        for i in range(len(givers)):
            giver = givers[i]
            receiver = random.choice(receivers)
            if (giver == receiver and i == (len(givers) - 1)):
                restart = True
                break
            else:
                while (receiver == giver):
                    receiver = random.choice(receivers)
                result.append(giver + ' -----> '+ receiver)
                receivers.remove(receiver)
                
    for r in result:
        print(r)

def main():
    dataFormatChoice()
    

if __name__ == '__main__':
    main()