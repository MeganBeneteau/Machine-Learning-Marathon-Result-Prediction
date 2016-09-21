%%%%%%%%%%%%DATA LOADING%%%%%%%%%%%%
data = load('finalData.csv');
Data = data(2:end, 2:end); %all the data
[n, numColumns] = size(A); %n = number of participants
m = numColumn - 1; %nmumber of features

k = 5; %num of folds
foldSize = n/k; %size of folds
foldId = kron( 1:k, ones(1,foldSize) );

for i = 1 : k
    %%% form train and test data %%%%
    trainId = find( foldId == i );
    testId  = find( foldId ~= i );
    train = Data(trainId, :);
    test = Data(testId, :); 
    
    w = log_reg(train,m); %% get weights from trainX
    predError = predictionError(w, test); %% find prediction error for iteration
    disp(predError);
    
end





