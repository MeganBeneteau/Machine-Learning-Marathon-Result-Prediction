W =[-3.5728; 0.8296; -18.8800; 0.7635; -4.4599; 39.4070; -6.2593; 4.9598];

%%%%%%%%%%%%DATA LOADING%%%%%%%%%%%%
data = load('realData.csv');

%%%%%%%%%%%%%%%%%%%%%INITIALIZE ARRAYS%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
m = 8; %num of features
predict = data(2:end, 2:10); %Y1 data
X = predict(:, 1:m); %input data, n x m, features
n = 8711;

%%%%%%%%% APPLY WEIGHTS ON PREDICTIVE DATA%%%%%%%%%%%%%%%%%%%%%%%%
results = zeros(n, 1); %hold resuls
numrunning = 0;
for c = 1:n
   temp = logistic_function(X(c,:) * W);
   if temp > 0.5
       results(c) = 1;
       numrunning = numrunning + 1;
   else
       results(c) = 0;
   end
end

csvwrite('Y1_predictions.csv',results);

