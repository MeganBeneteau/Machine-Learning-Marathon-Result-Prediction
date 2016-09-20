%%%%%%%%%%%%DATA LOADING%%%%%%%%%
%data = load('MontrealMarathon.txt');
%m = 3; %number of features
%n = 100;%number of participants
%X = data(:, 1:m); %input data, n x m, features
%Y = data(:, m+1); % output data, n x 1, 1=yes attended 2015 marathon, 0=no

%%%%% K-FOLD CROSS VALIDATION %%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

X = [1,1,1,1,1,1,1,1,1,1;
    2,2,2,2,2,2,2,2,2,2;
    3,3,3,3,3,3,3,3,3,3;
    4,4,4,4,4,4,4,4,4,4;
    5,5,5,5,5,5,5,5,5,5;
    6,6,6,6,6,6,6,6,6,6;
    7,7,7,7,7,7,7,7,7,7;
    8,8,8,8,8,8,8,8,8,8;
    9,9,9,9,9,9,9,9,9,9;
    10,10,10,10,10,10,10,10,10,10];

k = 5; %num of folds
foldSize = 2; %size of folds
foldId = kron( 1:k, ones(1,foldSize) );

for i = 1 : k
    trainIdx = find( foldId == i );
    testIdx  = find( foldId ~= i );
    trainX = X(trainIdx, :);
    testX = X(testIdx, :);
    disp(trainX);
    disp(testX);
end

