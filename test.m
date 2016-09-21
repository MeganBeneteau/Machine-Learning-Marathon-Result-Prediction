%%%%%%%%%%%%DATA LOADING%%%%%%%%%%%%
data = load('lis_ata.csv');

Data = data(2:end, 10); %all the data
[m,n] = size(Data); 
