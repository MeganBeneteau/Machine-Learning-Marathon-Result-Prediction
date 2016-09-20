%%%%%%%%%%%%DATA LOADING%%%%%%%%%%%%
%data = load('MontrealMarathon.txt');
X = data(:, :); %all the data
[n, numColumns] = size(A); %n = number of participants
m = numColumn - 1; %nmumber of features

k = 5; %num of folds
foldSize = n/k; %size of folds
foldId = kron( 1:k, ones(1,foldSize) );

for i = 1 : k
    %%% form train and test data %%%%
    trainIdx = find( foldId == i );
    testIdx  = find( foldId ~= i );
    trainX = X(trainIdx, :);
    testX = X(testIdx, :); 
    
    w = log_reg(trainX,m); %% get weights from trainX
    predictionError(w, testX); %% find prediction error for iteration
    
end





