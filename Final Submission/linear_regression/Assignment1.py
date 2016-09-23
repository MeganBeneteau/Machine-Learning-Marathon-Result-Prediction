import numpy as np
import pandas as pd
import csv
import sys

# Set up the maximum recursive depth
sys.setrecursionlimit(5000) 


print('Testing...')
# Set up the initial Value
# number of participants, step size, number of features and stop threshold
# Initialize the Weights

Crit=0.0001
feature_num=8
W_int=np.array([0.45,0.2,0.3,0.5,0.2,0.2,0.2,0.5,0.1])

# Read the data
from numpy import genfromtxt
my_data = genfromtxt('GoodData.csv', delimiter=',')
par_num=len(my_data)

#print my_data
#print len(my_data)
#print type(my_data)
#print type(my_data[1][2])

# Import the data to X_transp and Y
X_trans=my_data;
Y=np.arange(len(my_data),dtype=float)

for i in range (0,par_num):
    Y[i]=float(my_data[i][feature_num])
    X_trans[i][feature_num]=1

# Get X from X_transpose
X=X_trans.transpose()

# Implementing the d(error)/d(W)
X_trans_X=np.dot(X,X_trans)
Back=np.dot(Y,X_trans)

# K is the paremeter in the step size function 
k=0
# Caculate the Derivate of Error over W
def findNextW(W):
    global k
    k=k+1
    Front=np.dot(W,X_trans_X)
    Error=2*(Front-Back)
    #print "Front"
    #print Front
    #print "Back is"
    #print Back
    #print "Error is"
    #print Error
    next=W-(1.0/(k+1)/2000)*Error
    #print "The next is"
    #print next
    return next
    
W_new=np.arange(len(W_int),dtype=float)


# The recursive function that keeps recalculating new W if the Current W is smaller than the stop threshold. 
def recursive (W):
    global W_new
    W_temp=findNextW(W)
    if (np.sum(np.square(W_temp-W)))>Crit:
        print W_temp
        recursive (W_temp)
     
    else:
        print "The result is"
        W_new=W_temp

            
recursive (W_int)
print W_new
# Calculate the predicted Y
predic=np.dot(W_new,X)


# Assign -1 to participants who never run before
for i in range (0,(len(Y))):
     if Y[i]==0:
        predic[i]=-1
     #else:

# Change the Y from hours to seconds
for i in range (0,(len(Y))):
    if predic[i]!=-1:
        predic[i]=predic[i]*3600

     
print "True predic is"
print predic   

# Export the file to an csv file
np.savetxt("GoodPrediction.csv", predic, delimiter=",")


# Model Error Calculation ---------------------------------------------------------------------------------------------------------------- 
#for i in range (0,(len(Y))):
#    if predic[i]!=-1:
#        predic[i]=(abs(Y[i]-predic[i]))/Y[i]


#count=0
#sum=0.0
#for i in range (0,(len(Y))):
#    global count
#    global sum
#    if predic[i]!=-1:
#        count=count+1
#        sum=predic[i]/3600+sum

#print "mean"
#print sum/count

