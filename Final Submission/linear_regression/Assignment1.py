import numpy as np
import pandas as pd
import csv
import sys

# Set up the maximum recursive depth
sys.setrecursionlimit(5000) 


print('Training...')
# Set up the initial Value
# number of participants, step size, number of features and stop threshold
# Initialize the Weights

Crit=0.01
feature_num=8
W_int=np.array([0.45,0.2,0.3,0.5,0.2,0.2,0.2,0.5,0.1])

# Read the data
from numpy import genfromtxt
my_data = genfromtxt('TrainData_Conjugate.csv', delimiter=',')
par_num=len(my_data)
preY_num=0
for i in range (0,par_num):
    global preY_num
    if my_data[i][feature_num]!=0:
        preY_num=preY_num+1


print preY_num
preY=np.arange(preY_num,dtype=float)
address=np.arange(preY_num,dtype=int)
preX=np.arange(preY_num*(feature_num+1), dtype=float).reshape(preY_num,(feature_num+1))



idx=0
for i in range (0,par_num):
    global idx
    if my_data[i][feature_num]!=0:
        preY[idx]=my_data[i][feature_num]
        address[idx]=i;
        idx=idx+1

print "Address"
print address

for i in range (0,len(address)):
    for j in range (0, feature_num+1):
        preX[i][j]=my_data[address[i]][j]

print "preX is"
print preX
        

# Import the data to X_transp and Y
X_trans=preX
print "X_trans shape is"
print X_trans
Y=preY
print np.shape(Y)
#Y=np.arange(len(my_data),dtype=float)

for i in range (0,preY_num):
    Y[i]=float(X_trans[i][feature_num])
    X_trans[i][feature_num]=1.0
print "Y is"
print Y

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
    next=W-(1.0/(k+1)/3000)*Error
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
        print "The new weigth vector is"
        W_new=W_temp

            
recursive (W_int)
print W_new

# Calculate the predicted Y bsaed on the training data set
predic=np.dot(W_new,X)

predic_aft=np.arange(len(my_data),dtype=float)
for i in range(0,len(predic)):
    predic_aft[address[i]]=predic[i]


print "Address"
print address

# Assign -1 to participants who never run before
#for i in range (0,(len(address))):
#     if predic_aft[i]<2:
#       predic_aft[i]=-1
     
print "predic_aft is"
print predic_aft

# Change the Y from hours to seconds
for i in range (0,(len(predic_aft))):
        predic_aft[i]=predic_aft[i]*3600

# Prediction on training data set     
print "Prediction on Training data is"
print predic_aft   

# Export the file to an csv file
np.savetxt("GoodPrediction.csv", predic_aft, delimiter=",")


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


# Testing the model  --------------------------------------------------------------------------------------------------------
print "Testing..."
from numpy import genfromtxt
my_TestData = genfromtxt('TestData.csv', delimiter=',')
par_numTest=len(my_TestData)

# count the players who has previous result
preYY_num=0
for i in range (0,par_numTest):
    global preYY_num
    if my_TestData[i][feature_num]!=0:
        preYY_num=preYY_num+1


preYY=np.arange(preYY_num,dtype=float)
address_Test=np.arange(preYY_num,dtype=int)
preXX=np.arange(preYY_num*(feature_num+1), dtype=float).reshape(preYY_num,(feature_num+1))

# Only search for the information of the player who has previous result
idx=0
for i in range (0,preYY_num):
    global idx
    if my_TestData[i][feature_num]!=0:
        preYY[idx]=my_TestData[i][feature_num]
        address_Test[idx]=i;
        idx=idx+1


for i in range (0,len(address_Test)):
    for j in range (0, feature_num+1):
        preXX[i][j]=my_TestData[address_Test[i]][j]

XX_trans=preXX
YY=preYY

for i in range (0,preYY_num):
    YY[i]=float(XX_trans[i][feature_num])
    XX_trans[i][feature_num]=1.0

XX=XX_trans.transpose()
predic_Test=np.arange(len(my_TestData),dtype=float)

# Generate the prediction
predic_Test = np.dot(W_new,XX)

# Merging the result of players with previous results and those who don't
predic_aft_Test=np.arange(len(my_TestData),dtype=float)
for i in range(0,len(predic_Test)):
    predic_aft_Test[address_Test[i]]=predic_Test[i]

# Presenting the final prediction 
print "Prediction on Testing data is"
print predic_aft_Test


