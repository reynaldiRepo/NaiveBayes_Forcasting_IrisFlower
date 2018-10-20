import csv
import numpy as np
import math

def read():  
    Table = []
    temp = []
    with open('iris.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            data=(','.join(row))
            data=data.split(",")
            for i in data:
                #print(i)
                temp.append(i)
            Table.append(temp)
            temp = []
    temp = Table[0]
    del(Table[0])
    print(Table)
    return Table


def indexClass(Table):
    IndClass=[]
    AtrSetosa=[];Atrvirginica=[];Atrversicolor=[]
    temp1=[];temp2=[];temp3=[]
    for i in range (len(Table[0])-1) :
        for j in range (len(Table)):
            #print(Table[j][i])
            if Table[j][len(Table[0])-1] == 'Iris-setosa':
               #print('x')
                temp1.append(float(Table[j][i]))
            elif Table[j][len(Table[0])-1] == 'Iris-virginica':
                #print('a')
                temp2.append(float(Table[j][i]))
            elif Table[j][len(Table[0])-1] == 'Iris-versicolor':
                #print('b')
                temp3.append(float(Table[j][i]))
        AtrSetosa.append(temp1); Atrvirginica.append(temp2); Atrversicolor.append(temp3)
        temp1=[]; temp2=[]; temp3=[]
    '''
    print(len(AtrSetosa[0]),len(AtrSetosa[1]),len(AtrSetosa[2]))
    print(len(Atrvirginica[0]),len(Atrvirginica[1]),len(Atrvirginica[2]))
    print(len(Atrversicolor[0]),len(Atrversicolor[1]),len(Atrversicolor[2]))
    '''
    return AtrSetosa,Atrvirginica,Atrversicolor
           
def DeviasiMean(Table,AtrSetosa,Atrvirginica,Atrversicolor):
    temp=0
    temp2=0
    meanAtrSetosa=[];meanAtrvirginica=[];meanAtrversicolor=[]
    StdDAtrSetosa=[];StdDAtrvirginica=[];StdDAtrversicolor=[]
    for i in AtrSetosa :
        temp=np.std(i,ddof=1)
        temp2=np.mean(i)
        StdDAtrSetosa.append(temp)
        meanAtrSetosa.append(temp2)
        temp=0;temp2=0
    for i in Atrvirginica :
        temp=np.std(i,ddof=1)
        temp2=np.mean(i)
        StdDAtrvirginica.append(temp)
        meanAtrvirginica.append(temp2)
        temp=0;temp2=0
    for i in Atrversicolor :
        temp=np.std(i,ddof=1)
        temp2=np.mean(i)
        StdDAtrversicolor.append(temp)
        meanAtrversicolor.append(temp2)
        temp=0;temp2=0
    '''
    print(StdDAtrSetosa)
    print(StdDAtrvirginica)
    print(StdDAtrversicolor)
    print(meanAtrSetosa)
    print(meanAtrvirginica)
    print(meanAtrversicolor)
    '''
    return [meanAtrSetosa, meanAtrvirginica, meanAtrversicolor], [StdDAtrSetosa, StdDAtrvirginica, StdDAtrversicolor]

def pxyz(Table):
    setosa=0;virginica=0;versicolor=0
    for i in range (len(Table[0])-1) :
        for j in range (len(Table)):
            if Table[j][len(Table[0])-1] == 'Iris-setosa':
                setosa+=1
            elif Table[j][len(Table[0])-1] == 'Iris-virginica':
                virginica+=1
            elif Table[j][len(Table[0])-1] == 'Iris-versicolor':
                versicolor+=1
    setosa /=len(Table)
    virginica /=len(Table)
    versicolor /=len(Table)
    return setosa, virginica, versicolor

def NaiveBayes(Table ,w, x, y, z, DeviasiMean, pxyz):
    temp=[]
    norm1=0;norm2=0;norm3=0;norm4=0
    for i in range(len(Table[0])-2):
        norm1 = (1/(2*math.pi*(DeviasiMean[1][i][0]**2))**1/2)*math.exp(1)**((-1*(w-DeviasiMean[0][i][0])**2)/(2*DeviasiMean[1][i][0]**2))
        norm2 = (1/(2*math.pi*(DeviasiMean[1][i][1]**2))**1/2)*math.exp(1)**((-1*(x-DeviasiMean[0][i][1])**2)/(2*DeviasiMean[1][i][1]**2))
        norm3 = (1/(2*math.pi*(DeviasiMean[1][i][2]**2))**1/2)*math.exp(1)**((-1*(y-DeviasiMean[0][i][2])**2)/(2*DeviasiMean[1][i][2]**2))
        norm4 = (1/(2*math.pi*(DeviasiMean[1][i][3]**2))**1/2)*math.exp(1)**((-1*(z-DeviasiMean[0][i][3])**2)/(2*DeviasiMean[1][i][3]**2))
        temp.append(norm1*norm2*norm3*norm4*pxyz[i])
        norm1=0;norm2=0;norm3=0;norm4=0
    forcast=max(temp)
    forcastind=temp.index(forcast)
    if forcastind == 0:
        return 'Iris-setosa'
    elif forcastind == 1:
        return 'Iris-virginica'
    elif forcastind == 2:
        return 'Iris-versicolor'
    
def forcasting():
    a=read()
    b=indexClass(a)
    c=DeviasiMean(a,b[0],b[1],b[2])
    print (c[1])
    px=pxyz(a)
    w = float(input('sepallength : '))
    x = float(input('sepalwidth : '))
    y = float(input('petallength : '))
    z = float(input('petallength : '))
    print(NaiveBayes(a,w,x,y,z,c,px))

forcasting()                
                
            
