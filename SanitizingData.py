import re 
import datetime
def getTimeInSeconds(time):
	if len(time) == 8:
		h,m,s = re.split(':',time)
		timeInSeconds = int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())
	else:
		timeInSeconds = 0
	return timeInSeconds

def incrementYearAndTime (entry, date, raceLength,time):
	date = date[0:4]
	date = int(date)
	if date == 2015 and raceLength ==42:
			entry[9] = 1
	if date != 2015 and raceLength == 42:
		entry[1] = entry[1] + 1
		
		timeInSeconds = getTimeInSeconds(time)
		entry[10] = entry[10] + timeInSeconds #add the total, compute average later
	elif date == 2014:
		if raceLength == 42:
			timeInSeconds = getTimeInSeconds(time)
			if timeInSeconds != 0:
				entry[5] = entry[5] +1
				entry[1] = entry[1] +1
				entry[11] = entry[11]+timeInSeconds
		elif raceLength == 21:
			timeInSeconds = getTimeInSeconds(time)
			if timeInSeconds != 0:
				entry[6] = entry[6] +1
				entry[12] = entry[12]+timeInSeconds
		elif raceLength == 10:
			timeInSeconds = getTimeInSeconds(time)
			if timeInSeconds != 0:
				entry[7] = entry[7] +1
				timeInSeconds = getTimeInSeconds(time)
				entry[13] = entry[13]+timeInSeconds
		elif raceLength == 5:
			timeInSeconds = getTimeInSeconds(time)
			if timeInSeconds !=0:
				entry[8] = entry[8] +1
				timeInSeconds = getTimeInSeconds(time)
				entry[14] = entry[14]+timeInSeconds
	return entry

def computeAverages(entry):
	average =0;
	average = (42*entry[5])+(21*entry[6])+(10*entry[7])+(5*entry[8])
	if average !=0:
		average = average/(entry[5]+entry[6]+entry[7]+entry[8])
	entry[3] = average
	if entry[5] != 0:
		entry[11]=entry[11]/entry[5]
	if entry[6] != 0:
		entry[12]= entry[12]/entry[6]
	if entry[7] != 0:
		entry[13]=entry[13]/entry[7]
	if entry[8] != 0: 
		entry[14]=entry[14]/entry[8]
	return entry
import csv
#x=[] This will be the result
eventNames=[];
resultingData = [];
otherCategories = [];
result = [];
fiveKmNames=['5 KM', '5 km', '5 km Course/Marche', '5km Sports Experts','5 km Pneu Patry', '5 km Sports Experts', '5km Course'
,'Ottawa 5K', '5 Km', '5km Course et Marche','5 km - Course', '5K', '5 KM FAMILIPRIX', '5K Course','5 KM Marche'
,'5 km course','5 km Run-Walk', '5 km (Course)', '5 km Course', 'HTG Sports 5K', '5km Run/Walk', '5 Km- Physio Sante',
'5km', '5 Km Route', '5 km - D\xc3\xa9fi des entreprises', '5k', '5 km - Buropro', '5K Run - Course de 5K','Funnybone Run 5K'
, '5km Marche', '5K Run', '5 km Run','5 km Poussettes', 'Johnson 5km', '5 km Run and Walk', '5 km route',
'5 km Course et Marche', '5km Raquette', '5 km Marche', 'Canadian 5km Road Race Championship', '5 km - course',
'Canada Day 5k', '5 km - Canicourse', 'Co operators 5km', 'Course 5 km', '5 km Raquette', '5 KM INDIVIDUEL PARTICIPATIF',
'5km Run','Nage 5 km','Defi Asics 5km Course', '5 km (vendredi)','Barbados 5km'];
tenKmNames=['10 KM','10 km','10 km Oasis','Ottawa 10K','10K','10Km','10km','10 km - Physio Sante','10 km du Vignoble Les Petits Cailloux',
'10km Course','10k (Marathoners)','10 km - course','10 KM SIMARD','10 km route','Mercedes-Benz Oakville 10k','10k (Half Marathoners)',
'10 Km', 'Lowertown Brewery Ottawa 10K', 'MNP 10KM Run','10 km run/walk', '10 km (Course)', '10 Km Route', '10K Course',
'10 km course', '10 KM de Nuit', '10 km Physio Sante', '10 Km- Bourret', 'Minto Chapman Mills 10km', '10 km - Course',
'GoodLife Fitness 10k', 'Goodlife Fitness 10km', '10 km Course', '10 km Wishbone', '10 Km Course', '10 km Run', 'Course 10 km',
'Jan Nordstrom 10 km classique', 'JAN NORDSTROM 10KM CLASSIQUE', 'Jan Nordstrom 10 km Classique', '10 KM OCEAN','10 KM COURSE',
'10 KM Microbrasserie des Beaux Pr\xc3\xa9s', 'Wishbone Race 10K', 'UPS 10 km', 'Coure 10 Km', 'TRAIL RUN 10 KM', '10 KM DE NUIT VIZIBL'
 '10km Run Walk', '10k', 'Defi Asics 10km Course', '10km Chaussures Mille-pattes', '10km Run', '10 km de nuit', '10 km Run/Walk',
 '10 km de nuit', '10 KM Route', '10 km Style Libre', 'Course a pied - 10 km', '10K Run', 'Jan Nordstrom 10km Classique'];
marathonNames=['Marathon','Scotiabank Ottawa Marathon','Full Marathon', 'Friendly Massey Marathon','Scotiabank Full Marathon'
'Challenge Marathon', '42.2km', 'Saskatchewan Credit Unions 42.2K Run', 'Scotiabank Full Marathon', 'Challenge Marathon',
'AMJ Campbell Full Marathon','Marathon Beauceron'];
hafMarathonNames=['Ottawa Half Marathon','Demi-Marathon','Half Marathon','Demi Marathon','Ottawa Marathon','Demi-marathon'
, 'Scotiabank Ottawa Half Marathon', '1/2 Marathon - Demi-marathon', 'Demi marathon','Demi Marathon Course','Half Marathon - Demi Marathon'
'Auto Value Hyundai Half-Marathon Run', 'Recharge with Milk Half Marathon', 'Ottawa Half-Marathon - Demi-marathon',
'Half Marathon Run', 'DEMI-MARATHON','Half-Marathon','Recharge with Milk Half Marathon Run','Demi Marathon Podiatre Elizabeth'
, '21 km', '21 KM', '21.1 km', '21.1km', '21.1 KM CARON ET GUAY', '21 km - course', '21km Course','21 km (Course)','Half Marathon - Demi Marathon'
 'Vittoria Trattoria Half Marathon','The Canadian Evening Half-Marathon','Demi-marathon Podiatre Elizabeth','Demi Marathon Marche',
 'Auto Value Hyundai Half-Marathon Run','Demi-Marathon du crepuscule - 21 km (19.5 km)','RE/MAX Qunite Half Marathon' ,'Nutrience Half Marathon',
 'Demi Marathon 21.1km','DEMI-MARATHON 21.1 KM','Siskinds Half Marathon Run','Nutrience Half Marathon Run'];
numberOf5k=0;

numberOf10k=0;
numberOfMarathon=0;
numberOfHalfMarathon=0;
categories = []
with open('Project1_data.csv', 'rb') as csvfile:
	dialect = csv.Sniffer().sniff(csvfile.read(1024))

	csvfile.seek(0)
	reader = csv.reader(csvfile, dialect)
	#print csv.reader.dialect
	for row in reader:
		entry = [None,0,None,0,0,0,0,0,0,0,0,0,0,0,0]
		columns=len(row)
		currentRaceEvaluated=3
		currentTimeEvaluated = 4
		currentGenderEvaluated=5
		numberMarathonsRun=0
		currentDateEvaluated=1
		entry[0]=row[0] #copy identity

		while (columns > currentRaceEvaluated):

			if row[currentRaceEvaluated] in tenKmNames:
				numberOf10k=numberOf10k+1
				entry = incrementYearAndTime(entry, row[currentDateEvaluated], 10, row[currentTimeEvaluated])
		
			elif row[currentRaceEvaluated] in fiveKmNames:
				numberOf5k=numberOf5k+1;
				entry = incrementYearAndTime(entry, row[currentDateEvaluated], 5,row[currentTimeEvaluated])
				#row[currentEvaluated] = 5

			elif row[currentRaceEvaluated] in marathonNames:
				numberOfMarathon=numberOfMarathon+1
				#row [currentEvaluated] = 42 #insert 42 km as amount run
				numberMarathonsRun = numberMarathonsRun +1;
				entry = incrementYearAndTime(entry, row[currentDateEvaluated], 42,row[currentTimeEvaluated])
		
			elif row[currentRaceEvaluated] in hafMarathonNames:
				numberOfHalfMarathon=numberOfHalfMarathon+1;
				entry = incrementYearAndTime(entry, row[currentDateEvaluated], 21,row[currentTimeEvaluated])
				#row [currentRaceEvaluated] = 21	
		
			elif row[currentRaceEvaluated] not in eventNames: #2 is the race name, 3 is the length
				eventNames.append(row[currentRaceEvaluated]) #track which have been left out
			currentRaceEvaluated = currentRaceEvaluated + 5
			currentDateEvaluated = currentDateEvaluated + 5
			currentTimeEvaluated = currentTimeEvaluated + 5

		if columns -1 >= currentGenderEvaluated and len(row[currentGenderEvaluated])>0:
			category = row[currentGenderEvaluated]
			gender = category[0]
			ageLength = len(category)
			ageGroup = category[1:ageLength]
			if gender not in ('F','m','M','f','H'):
				otherCategories.append(category)
				entry[2] = -1
			else:
				if gender in ('H','M','m'): #men so 1
					entry[2] = 1
				else:
					entry[2] = 0
			if ageGroup not in categories:
				categories.append(ageGroup)
		entry = computeAverages(entry)
		result.append(entry)
print categories
print len(categories)
with open('trainingData.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                             quoting=csv.QUOTE_MINIMAL)
    for dataEntry in result:
    	writer.writerow(dataEntry)
count = 0
count2 =0
for dataEntry in result:
		if dataEntry[9] ==1:
			count = count +1
		else:
			count2 = count2 +1
print count
print count2
