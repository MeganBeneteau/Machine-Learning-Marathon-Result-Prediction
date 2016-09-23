function [W] = log_reg(train,m)

%%%%%%%%%%%%%%%%%%%%%INITIALIZE ARRAYS%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
X = train(:, 1:m); %input data, n x m, features
Y = train(:, m+1); % output data, n x 1, 1=yes attended 2015 marathon, 0=no
W = rand(m,1); %initialize Weights array

%%%%%%%%%%%%%%%%%%%% Gradient Descent %%%%%%%%%%%%%%%%%%%%%%%%%%%%
iters = 500;

n = size(train,1); %number of participants in trainX

for k=1: iters
   lf = zeros(m,1);
   for i=1:n %loop through samples
        lf = lf + (logistic_function(X(i,:) * W) - Y(i)) * X(i,:)';
   end
   W = W - (1.0/(k+1)) * lf;
end

%%% find error on train%%%
%%%%%%%%% X Results%%%%%%%%%%%%%%%%%%%%%%%%
results = zeros(n, 1); %hold resuls
for c = 1:n
   temp = logistic_function(X(c,:) * W);
   if temp > 0.5
       results(c) = 1;
   else
       results(c) = 0;
   end
end

match = 0; %number of times it's a match
for k=1:n %loop through participants
    if results(k) == Y(k)
        match = match+1; %how many are matches
    end
end

TrainError=(1-(match/n));

disp('Train Error');
disp(TrainError);
end

