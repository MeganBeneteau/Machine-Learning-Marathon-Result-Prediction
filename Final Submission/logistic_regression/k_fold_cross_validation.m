%%%%%%%%%%%%DATA LOADING%%%%%%%%%%%%
data = load('trainingData.csv');
m = 8; %num of features
n = 8711; %num of participants
Data = data(2:end, 2:10); %Y1 data

k =5; %num of folds
foldSize = round(n/k) -1; %size of folds
foldId = kron( 1:k, ones(1,foldSize) );

for i = 1 : k

    disp('Round:');
    disp(i);
    
    %%% form train and test data %%%%
    trainId = find( foldId == i );
    testId  = find( foldId ~= i );
    train = Data(trainId, :);
    test = Data(testId, :); 
    
    w = log_reg(train,m); %% get weights from trainX
    
    predError = predictionError(w, test,m); %% find prediction error for iteration
    
    disp('Validation Error:')
    disp(predError);
    
    disp('Weights:');
    disp(w);
end







