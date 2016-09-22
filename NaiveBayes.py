from __future__ import division
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
	pNotRanHalfMarathonIn2014=0
	pNotRanNoHalfMarathonIn2014=0
	dialect = csv.Sniffer().sniff(csvfile.read(1024))

	csvfile.seek(0)
	reader = csv.reader(csvfile, dialect)
	for row in reader:
	
		if row[9] == '1':
			pRan=pRan+1
			if row[2] == '0':
				pRanWoman =pRanWoman +1
			else:
				pRanMale = pRanMale +1
			if int(row[1]) > 0:
 				pRanHadMarathonExperience = pRanHadMarathonExperience +1
			else:
				pRanHadNoMarathonExperience = pRanHadNoMarathonExperience +1
			if int(row[5]) > 0:
				pRanMarathonIn2014 = pRanMarathonIn2014 +1
			else:
				pRanNoMarathonIn2014 = pRanNoMarathonIn2014 + 1
			if int(row[6]) > 0:
				pRanHalfMarathonIn2014 = pRanHalfMarathonIn2014 +1
			else:
				pRanNoHalfMarathonIn2014 = pRanNoHalfMarathonIn2014 + 1

		else:
			pNotRan=pNotRan+1
			if row[2] == '0':
				pNotRanWoman =pNotRanWoman +1
			else:
				pNotRanMale = pNotRanMale +1
			if int(row[1]) > 0:
				pNotRanHadMarathonExperience = pNotRanHadMarathonExperience +1
			else:
				pNotRanHadNoMarathonExperience = pNotRanHadNoMarathonExperience +1
			if int(row[5]) > 0:
				pNotRanMarathonIn2014 = pNotRanMarathonIn2014 +1
			else:
				pNotRanNoMarathonIn2014 = pNotRanNoMarathonIn2014 + 1
			if int(row[6]) > 0:
				pNotRanHalfMarathonIn2014 = pNotRanHalfMarathonIn2014 +1
			else:
				pNotRanNoHalfMarathonIn2014 = pNotRanNoHalfMarathonIn2014 + 1
		
print "Ran if woman: "+str(pRanWoman)+"/"+str(pRan)
print "Ran if male : "+str(pRanMale)+"/"+str(pRan)
print "Ran if they had ever run a marathon"+str(pRanHadMarathonExperience)+"/"+str(pRan)
print "Ran if they had never run a marathon"+str(pRanHadNoMarathonExperience)+"/"+str(pRan)
print "Ran if they had ran a marathon last year:"+str(pRanMarathonIn2014) +"/"+str(pRan)
print "Ran if they did not run a marathon last year"+str(pRanNoMarathonIn2014)+"/"+str(pRan)
print "Ran if they ran a half marathon last year"+str(pRanHalfMarathonIn2014)+"/"+str(pRan)
print "Ran if they did not run a half marathon last year"+str(pRanNoHalfMarathonIn2014)+"/"+str(pRan)
print "Did not Run if woman: "+str(pNotRanWoman)+"/"+str(pNotRan)
print "Did not Run if male : "+str(pNotRanMale)+"/"+str(pNotRan)
print "Did not Run  if they had ever run a marathon"+str(pNotRanHadMarathonExperience)+"/"+str(pNotRan)
print "Did not Run if they had never run a marathon"+str(pNotRanHadNoMarathonExperience)+"/"+str(pNotRan)
print "Did not Run if they had ran a marathon last year:"+str(pNotRanMarathonIn2014) +"/"+str(pNotRan)
print "Did not Run if they did not run a marathon last year"+str(pNotRanNoMarathonIn2014)+"/"+str(pNotRan)
print "Did not Run if they ran a half marathon last year"+str(pNotRanHalfMarathonIn2014)+"/"+str(pNotRan)
print "Did not Run if they did not run a half marathon last year"+str(pNotRanNoHalfMarathonIn2014)+"/"+str(pNotRan)
with open('trainingData.csv', 'rb') as csvfile:
	dialect = csv.Sniffer().sniff(csvfile.read(1024))

	csvfile.seek(0)
	reader = csv.reader(csvfile, dialect)
	results=[]
	total = pRan+pNotRan
	will= 0
	wont=0
	correct=0
	count =0
	for row in reader:
		pTheyWill=1
		pTheyWont=1
		
		result= [0,0]
		result[0]=row[0]
		if row[2] == '0':
			pTheyWill=pTheyWill*(pRanWoman/pRan)
			pTheyWont=pTheyWont*(pNotRanWoman/pNotRan)
		else:
			pTheyWill=pTheyWill*(pRanMale/pRan)
			pTheyWont=pTheyWont*(pNotRanMale/pNotRan)
		if int(row[1]) > 0:
 			pTheyWill=pTheyWill* (pRanHadMarathonExperience/pRan)
 			pTheyWont=pTheyWont* (pNotRanHadMarathonExperience/pNotRan)
		else:
			pTheyWill =pTheyWill* (pRanHadNoMarathonExperience/pRan)
			pTheyWont =pTheyWont* (pNotRanHadNoMarathonExperience/pNotRan)
		if int(row[5]) > 0:
			pTheyWill=pTheyWill*(pRanMarathonIn2014/pRan)
			pTheyWont=pTheyWont*(pNotRanMarathonIn2014/pNotRan)
		else:
			pTheyWill =pTheyWill* (pRanNoMarathonIn2014/pRan)
			pTheyWont =pTheyWont* (pNotRanNoMarathonIn2014/pNotRan)
		if int(row[6]) > 0:
			pTheyWill = pTheyWill*(pRanHalfMarathonIn2014/pRan)
			pTheyWont= pTheyWont*(pNotRanHalfMarathonIn2014/pNotRan)
		else:
			pTheyWill=pTheyWill* (pRanNoHalfMarathonIn2014/pRan)
			pTheyWont=pTheyWont*(pNotRanNoHalfMarathonIn2014/pNotRan)

		pTheyWill=pTheyWill*(pRan/total)
		pTheyWont=pTheyWont*(pNotRan/total)

		if pTheyWill > pTheyWont:
			result[1]=1
			will=will+1
		else:
			result[1]=0
			wont = wont+1
		
		if count >= 1 and count <20:
			print "person"
			print result[0]
			print result[1]

		if int(row[9]) == result[1]:
			correct = correct+1
		results.append(result)
		count = count +1
print will
print wont
print correct/total
