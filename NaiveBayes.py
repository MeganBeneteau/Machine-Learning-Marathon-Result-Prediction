with open('trainingData', 'rb') as csvfile:
	pRan =0 
	pNotRan =0
	pRanMale=0
	pRanWoman=0
	pNotRanMale=0
	pNotRanWoman=0
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
			pRan=pRan+1
			if row[2] = 0:
				pRanWoman =pRanWoman +1
			else:
				pRanMale = pRanMale +1
			if row[1] >0
 				pRanHadMarathonExperience = pRanHadMarathonExperience +1
			else:
				pRanHadNoMarathonExperience = pRanHadNoMarathonExperience +1
		else:
			pNotRan=pNotRan+1
			if row[2] = 0:
				pNotRanWoman =pNotRanWoman +1
			else:
				pNotRanMale = pNotRanMale +1
			if row[1] >0
				pNotRanHadMarathonExperience = pNotRanHadMarathonExperience +1
			else:
				pNotRanHadNoMarathonExperience = pNotRanHadNoMarathonExperience +1