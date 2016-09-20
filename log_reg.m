function [W] = log_reg(train,m)

%%%%%%%%%%%%%%%%%%%%%INITIALIZE ARRAYS%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
X = train(:, 1:m); %input data, n x m, features
Y = train(:, m+1); % output data, n x 1, 1=yes attended 2015 marathon, 0=no
W = rand(m,1); %initialize Weights array

%%%%%%%%%%%%%%%%%%%% Gradient Descent %%%%%%%%%%%%%%%%%%%%%%%%%%%%
alpha = .005; %??????
iters = 500;

n = size(train,1); %number of participants in trainX

for k=1: iters
   lf = zeros(m,1);
   for i=1:n %loop through samples
        lf = lf + (logistic_function(X(i,:) * W) - Y(i)) * X(i,:)';
   end
   W = W - alpha * lf;
end

end

