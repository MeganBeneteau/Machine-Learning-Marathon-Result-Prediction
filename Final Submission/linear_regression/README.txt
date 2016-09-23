CSV Files:

    GoodData.csv - data with features to predict Marathon 2016
    GoodPredictions.csv - holds predictions for Y1_Logistic
	ValidationData.csv - data used to validate weights for Marathon 2015
	TestData.csv - data to train the model to predict the result
	TrainData_Conjugate.csv - data used to train and test the model
	TestData.csv2 - data to test the model to predict the result
    
 
 How to Run Program:
 
 In order to train and test
    1. Run Assignment1.py . The data loaded is TestData.m and TrainData_Conjugate
 In order to predict the full result
	1. Run assingment1.py  at the top of the code, change the file loaded to GoodData.csv
	2. Comment out the everything below  --Model Error Calculation----
    2. GoodPredictions.csv will be created / updated with predictions