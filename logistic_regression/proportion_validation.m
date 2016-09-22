%%%%%%%%%%%%DATA LOADING%%%%%%%%%%%%
data = load('lis_data.csv');
m = 8; %num of features
n = 8711; %num of participants
Data = data(2:end, 2:10); %Y1 data

%%% form train and test data %%%%
train = Data(1:6000, :);
test = Data(6001:8711, :); 
    
w = log_reg(train,m); %% get weights from trainX
 
predError = predictionError(w, test,m); %% find prediction error for iteration

disp(w);
