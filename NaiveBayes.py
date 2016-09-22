import csv
with open('trainingData.csv', 'rb') as csvfile:
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
			if row[2] == 0:
				pRanWoman =pRanWoman +1
			else:
				pRanMale = pRanMale +1
			if row[1] > 0:
 				pRanHadMarathonExperience = pRanHadMarathonExperience +1
			else:
				pRanHadNoMarathonExperience = pRanHadNoMarathonExperience +1
			if row[5] > 0:
				pRanMarathonIn2014 = pRanMarathonIn2014 +1
			else:
				pRanNoMarathonIn2014 = pRanNoMarathonIn2014 + 1
			if row[6] > 0:
				pRanHalfMarathonIn2014 = pRanHalfMarathonIn2014 +1
			else:
				pRanNoHalfMarathonIn2014 = pRanNoHalfMarathonIn2014 + 1

		else:
			pNotRan=pNotRan+1
			if row[2] == 0:
				pNotRanWoman =pNotRanWoman +1
			else:
				pNotRanMale = pNotRanMale +1
			if row[1] > 0:
				pNotRanHadMarathonExperience = pNotRanHadMarathonExperience +1
			else:
				pNotRanHadNoMarathonExperience = pNotRanHadNoMarathonExperience +1
			if row[5] > 0:
				pNotRanMarathonIn2014 = pNotRanMarathonIn2014 +1
			else:
				pNotRanNoMarathonIn2014 = pNotRanNoMarathonIn2014 + 1
			if row[6] > 0:
				pNotRanHalfMarathonIn2014 = pNotRanHalfMarathonIn2014 +1
			else:
				pNotRanNoHalfMarathonIn2014 = pNotRanNoHalfMarathonIn2014 + 1
		
print "Ran if woman: "+pRanWoman+"/"+pRan
print "Ran if male : "+pRanMale+"/"+pRan
print "Ran if they had ever run a marathon"+pRanHadMarathonExperience+"/"+pRan
print "Ran if they had never run a marathon"+pRanHadNoMarathonExperience+"/"+pRan
print "Ran if they had ran a marathon last year:"+pRanMarathonIn2014 +"/"+pRan
print "Ran if they did not run a marathon last year"+pRanNoMarathonIn2014+"/"+pRan
print "Ran if they ran a half marathon last year"+pRanHalfMarathonIn2014+"/"+pRan
print "Ran if they did not run a half marathon last year"+pRanNoHalfMarathonIn2014+"/"+pRan
print "Did not Run if woman: "+pNotRanWoman+"/"+pNotRan
print "Did not Run if male : "+pNotRanMale+"/"+pNotRan
print "Did not Run  if they had ever run a marathon"+pNotRanHadMarathonExperience+"/"+pNotRan
print "Did not Run if they had never run a marathon"+pNotRanHadNoMarathonExperience+"/"+pNotRan
print "Did not Run if they had ran a marathon last year:"+pNotRanMarathonIn2014 +"/"+pNotRan
print "Did not Run if they did not run a marathon last year"+pNotRanNoMarathonIn2014+"/"+pNotRan
print "Did not Run if they ran a half marathon last year"+pNotRanHalfMarathonIn2014+"/"+pNotRan
print "Did not Run if they did not run a half marathon last year"+pNotRanNoHalfMarathonIn2014+"/"+pNotRan