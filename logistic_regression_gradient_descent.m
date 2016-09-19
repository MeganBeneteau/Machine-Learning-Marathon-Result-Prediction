%DATA LOADING
%data = load('MontrealMarathon.txt');
%X = data(:, 1:m); %input data, n x m, features
%Y = data(:, m+1); % output data, n x 1, 1=yes attended 2015 marathon, 0=no

%%%%%%%%%%%%%%%%%%%%%INITIALIZE ARRAYS%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
m = 3; %number of features
n = 100;%number of examples
d = rand(n,m+1);
disp(d);
X = d(:, 1:m); %input data, n x m, features
disp(X);
Y = d(:, m+1); % output data, n x 1, 1=yes attended 2015 marathon, 0=no
disp(Y);
W = rand(m,1); %initialize Weights array

%%%%%%%%%%%%%%%%%%%% Gradient Descent %%%%%%%%%%%%%%%%%%%%%%%%%%%%
alpha = .002; %??????
iters = 1000;

for k=1: iters
   lf = zeros(m,1);
   for i=1:n %loop through samples
        lf = lf + (logistic_function(X(i,:) * W) - Y(i)) * X(i,:)';
   end
   W = W - alpha * lf;
end

%%%%%%%%%%%%%%%%%%% CLASSIFY %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
results = zeros(n, 1); %hold resuls
for c = 1:n
   temp = logistic_function(X(c,:) * W);
   if temp > 0.5
       results(c) = 1;
   else
       results(c) = 0;
   end
end
    
disp(results);



