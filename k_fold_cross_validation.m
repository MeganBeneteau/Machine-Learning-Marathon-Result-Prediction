%%%%%%%%%%%%DATA LOADING%%%%%%%%%%%%
data = load('lis_ata.csv');
m = 8; %num of features
n = 8711; %num of participants
Data = data(2:end, 2:10); %all the data


k = 4; %num of folds
foldSize = round(n/k); %size of folds
disp(n);
disp(k);
disp(foldSize);
foldId = kron( 1:k, ones(1,foldSize) );

for i = 1 : k
    %%% form train and test data %%%%
    trainId = find( foldId == i );
    testId  = find( foldId ~= i );
    train = data(trainId, :);
    test = data(testId, :); 
    
    w = log_reg(train,m); %% get weights from trainX
 
    predError = predictionError(w, test,m); %% find prediction error for iteration
    disp(predError);
end







