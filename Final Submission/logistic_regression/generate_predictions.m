W =[288.5085; -14.1805; -6.4029; 0.5468; 0.5211; 3.1816; 15.2735; 11.7311];

%%%%%%%%%%%%DATA LOADING%%%%%%%%%%%%
data = load('realData.csv');

%%%%%%%%%%%%%%%%%%%%%INITIALIZE ARRAYS%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
m = 8; %num of features
predict = data(2:end, 2:10); %Y1 data

X = predict(:, 1:m); %input data, n x m, features

%%%%%%%%% APPLY WEIGHTS ON PREDICTIVE DATA%%%%%%%%%%%%%%%%%%%%%%%%
results = zeros(n, 1); %hold resuls
for c = 1:n
   temp = logistic_function(X(c,:) * W);
   if temp > 0.5
       results(c) = 1;
   else
       results(c) = 0;
   end
end

display(results);
csvwrite('Y1_predictions.csv',results);
