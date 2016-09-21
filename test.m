%%%%%%%%%%%%DATA LOADING%%%%%%%%%%%%
data = load('lis_data.csv');

Data = data(2:5, [10]); %all the data
disp(Data);
[m,n] = size(Data); 
