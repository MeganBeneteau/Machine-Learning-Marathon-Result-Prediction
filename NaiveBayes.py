with open('trainingData', 'rb') as csvfile:
	pRanMale=0
	pRanWoman=0
	pNotRanMale=0
	pNotRamWoman=0
	pRanHadMarathonExperience=0
	pRanHadNoMarathonExperience=0
	pNotRanHadMarathonExperience=0
	pNotRanHadNoMarathonExperience=0
	pRanMarathonIn2014=0
	pRanNoMarathonIn2014=0
	pNotRanMarathonIn2014=0
	pNotRanNoMarathonIn2014=0
	pRanHalfMarathonIn2014=0
	pRanNoHalfMarathonIn2014=0
	pNotRanHalfarathonIn2014=0
	pNotRanHalfNoMarathonIn2014=0
	dialect = csv.Sniffer().sniff(csvfile.read(1024))

	csvfile.seek(0)
	reader = csv.reader(csvfile, dialect)
	for row in reader:
		if row[9] == 1:
			if row[1] >0
				
		else:  
