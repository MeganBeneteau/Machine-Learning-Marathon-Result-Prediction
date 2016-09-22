These are the files used to do Logistic Regression with Gradient Descent for Y1. Matlab and CSV files were used. 

CSV Files:
    trainingData.csv - data used to train / validate weights for Marathon 2015
    realData.csv - data with features to predict Marathon 2016
    Y1_predictions.csv - holds predictions for Y1_Logistic
    
 
 How to Run Program:
 
    1. Run k_fold_cross_validation.m and select weights from best round with lowest Error(valid). N.B. k_fold_cross validation uses log_reg.m which predicts weights given training set and logistic_function.m is the actual sigmoid function. The data loaded is trainingData.m.
    2. Use those weights in generate_predictions.m which uses realData.m.
    3. Y1_predictions.csv will be created / updated with predictions
    
    