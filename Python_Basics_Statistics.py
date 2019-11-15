import numpy as np
from sklearn.model_selection import train_test_split
import random
import math 
import pandas as pd

n1=[]

#Create a matrix : n1
#size : 150; counter : 1

for i in range(0,125,1):
    n1.append(random.uniform(-4,4))
   
dataX=np.mat(n1)
dataX=dataX.reshape(25,5)

#Create a function to calculate the average
def avg(dataset):
    #Then convert from 1D(150 values array), : k array
    k=np.mat(dataset) 
    #to 2D(25x5 matrix) using reshape or shape function : k matrix
    k=k.reshape(25,5)
    k.shape
    #Create a new array for average(each row) : xx
    xx=[]
    
    for i in range(0,25,1):
        sm=0
        for j in range(0,5,1):
            sm+=k[i,j]    
        xx.append(sm/5)
    return xx

#Apply the function
dene=avg(dataX)

def standart_deviation(dataset):
    k=np.mat(dataset)
    k=k.reshape(25,5)
    yy=[]

    for i in range(0,25,1):
        kv=0
        for j in range(0,5,1):
            kv+=((dene[i])-k[i,j])**2    
        yy.append(math.sqrt(kv/4))
    return yy
 
std=standart_deviation(dataX)

#R value can be described that max number-min number in the series
def R(dataset):
    k=np.mat(dataset)
    k=k.reshape(25,5)
    R_Series=[]
    
    for i in range(0,25,1):
        R_value=0.0
        max_val=0
        min_val=0
        for j in range(0,5,1):
            if(k[i,j]>max_val):
                max_val=k[i,j]
            if(k[i,j]<min_val):
                min_val=k[i,j]
            R_value=max_val-min_val
        R_Series.append(R_value)
    return R_Series

R_Value=R(dataX)

#Create a new matrix to convert 1D to 2D : xy
rslt_avg=np.mat(dene)
rslt_avg.reshape(1,25)
rslt_avg=rslt_avg.transpose()

#Create a new matrix to convert 1D to 2D : xy
rslt_std=np.mat(std)
rslt_std.reshape(1,25)
rslt_std=rslt_std.transpose()

#Create a new matrix to convert 1D to 2D : xy
rslt_R=np.mat(R_Value)
rslt_R.reshape(1,25)
rslt_R=rslt_R.transpose()

#Then use the concatenate function
#to merge matrix k(random x values),xy(transpose the average values)
#assign the a
a=np.concatenate([dataX,rslt_avg,rslt_std,rslt_R],axis=1)

matrixA=pd.DataFrame(a)

writer = pd.ExcelWriter('Statistical-Process-Control-Dataset.xlsx', engine='xlsxwriter')
matrixA.to_excel(writer,'Sheet1')
writer.save()

