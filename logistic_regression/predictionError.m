function [ predError ] = predictionError( W, test, m)

X = test(:, 1:m); %input data, n x m, features
Y = test(:, m+1); % output data, n x 1, 1=yes attended 2015 marathon, 0=no
n = size(test,1); %number of participants in testX

%%%%%%%%% Find testX Results%%%%%%%%%%%%%%%%%%%%%%%%
results = zeros(n, 1); %hold resuls
for c = 1:n
   temp = logistic_function(X(c,:) * W);
   if temp > 0.5
       results(c) = 1;
   else
       results(c) = 0;
   end
end

%%%%%%%% Compare Results with Real Results %%%%%%%%%
match = 0; %number of times it's a match
running = 0; %percent running
for k=1:n %loop through participants
    if results(k) == Y(k)
        match = match+1; %how many are matches
    end
    if results(k) == 1
        running = running + 1;
    end
end

disp(running/n);

predError= 1 - (match/n);

