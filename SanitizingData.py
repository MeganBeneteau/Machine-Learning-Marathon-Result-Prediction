import csv
#x=[] This will be the result
eventNames=[];
currentEvaluated = 3;
fiveKmNames=['5 KM', '5 km', '5 km Course/Marche', '5km Sports Experts','5 km Pneu Patry', '5 km Sports Experts', '5km Course'
,'Ottawa 5K', '5 Km', '5km Course et Marche','5 km - Course', '5K', '5 KM FAMILIPRIX', '5K Course','5 KM Marche'
,'5 km course','5 km Run-Walk', '5 km (Course)', '5 km Course'];
tenKmNames=['10 KM','10 km','10 km Oasis','Ottawa 10K','10K','10Km','10km','10 km - Physio Sante','10 km du Vignoble Les Petits Cailloux',
'10km Course','10k (Marathoners)','10 km - course','10 KM SIMARD','10 km route','Mercedes-Benz Oakville 10k','10k (Half Marathoners)',
'10 Km', 'Lowertown Brewery Ottawa 10K', 'MNP 10KM Run','10 km run/walk'];
marathonNames=['Marathon','Scotiabank Ottawa Marathon','Full Marathon', 'Friendly Massey Marathon','Scotiabank Full Marathon'
'Challenge Marathon', '42.2km', 'Saskatchewan Credit Unions 42.2K Run'];
hafMarathonNames=['Ottawa Half Marathon','Demi-Marathon','Half Marathon','Demi Marathon','Ottawa Marathon','Demi-marathon'
, 'Scotiabank Ottawa Half Marathon', '1/2 Marathon - Demi-marathon', 'Demi marathon','Demi Marathon Course','Half Marathon - Demi Marathon'
'Auto Value Hyundai Half-Marathon Run', 'Recharge with Milk Half Marathon', 'Ottawa Half-Marathon - Demi-marathon',
'Half Marathon Run', 'DEMI-MARATHON','Half-Marathon','Recharge with Milk Half Marathon Run','Demi Marathon Podiatre Elizabeth'
, '21 km', '21 KM', '21.1 km', '21.1km', '21.1 KM CARON ET GUAY', '21 km - course', '21km Course','21 km (Course)'];
numberOf5k=0;
numberOf10k=0;
numberOfMarathon=0;
numberOfHalfMarathon=0;
with open('Project1_data.csv', 'rb') as csvfile:
	dialect = csv.Sniffer().sniff(csvfile.read(1024))
	csvfile.seek(0)
	reader = csv.reader(csvfile, dialect)
	for row in reader:
		if row[currentEvaluated] in tenKmNames:
			numberOf10k=numberOf10k+1
			row.insert(1,10) #insert 10 as number of run
		
		elif row[currentEvaluated] in fiveKmNames:
			numberOf5k=numberOf5k+1;
			row.insert(1,5)

		elif row[currentEvaluated] in marathonNames:
			numberOfMarathon=numberOfMarathon+1
			row.insert(1,42) #insert 42 km as amount run
		
		elif row[currentEvaluated] in hafMarathonNames:
			numberOfHalfMarathon=numberOfHalfMarathon+1;
			row.insert(1,21)	
		
		elif row[currentEvaluated] in eventNames: #2 is the race name, 3 is the length
			row.insert(1,0)
		
		else:
			eventNames.append(row[currentEvaluated])
			row.insert(1,0)
		#row.insert(0,"boo")
		#x.append(row)
print numberOf10k
print numberOf5k
print numberOfHalfMarathon
print numberOfMarathon
print numberOf5k+numberOf10k+numberOfHalfMarathon+numberOfMarathon