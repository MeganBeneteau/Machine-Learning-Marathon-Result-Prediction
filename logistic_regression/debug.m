%%%%%%%%%%%%DATA LOADING%%%%%%%%%%%%
data = load('lis_data.csv');
m = 8; %num of features
n = 30; %num of participants
Data = data(2:31, 2:10); %Y1 data

train = Data(10:30, :);
test = Data(1:9, :); 

w = log_reg(train,m); %% get weights from trainX

predError = predictionError(w, test,m); %% find prediction error for iteration
disp(predError);






