import csv
import sys

header = ["bizID", 
		  "bizCat", 
		  "bizCatSub", 
		  "bizName", 
		  "bizAddr", 
		  "bizCity", 
		  "bizState", 
		  "bizZip", 
		  "bizPhone", 
		  "bizEmail", 
		  "bizURL", 
		  "locLat", 
		  "locLong", 
		  "locCounty"]

outputFile = open('thriftstore-test.csv', 'w')

def newLine():
	outputFile.write("\n")

def delimit():
	outputFile.write(";")

for item in header:
	outputFile.write(item)
	delimit()
newLine()
rowIndex = 1
while (rowIndex <= 2000):
	indexStr = str(rowIndex)
	name = "Store Name " + indexStr
	address = indexStr + " Main Street, Apartment " + indexStr
	phone = "(205)425-1" + indexStr
	email = "www.titlecash" + indexStr + ".com"
	web = "www.goodwill.org"
	city = ""
	state = ""
	zipcode = ""
	county = ""
	lat = ""
	longitude = ""
	if rowIndex <= 500:
		city = "Los Angeles"
		county = "Los Angeles"
		state = "CA"
		zipcode = "90201"
		if rowIndex % 2 == 0:
			lat = str(float(34.052235) + float((rowIndex-1) * 0.002))
			longitude = str(float(-118.243683) - float((rowIndex-1) * 0.002))
		else:
			lat = str(float(34.052235) - float(rowIndex-1) * 0.002)
			longitude = str(float(-118.243683) + float((rowIndex-1) * 0.002))
	elif rowIndex <= 1000:
		city = "San Francisco"
		county = "San Francisco"
		state = "CA"
		if rowIndex % 2 == 0:
			zipcode = "94132"
			lat = str(float(37.773972) + float((rowIndex-1) * 0.002))
			longitude = str(float(-122.431297) - float((rowIndex-1) * 0.002))
		else:
			zipcode = "94104"
			lat = str(float(37.773972) - float((rowIndex-1) * 0.0015))
			longitude = str(float(-122.431297) + float((rowIndex-1) * 0.0015))
	elif rowIndex <= 1500:
		city = "Chicago"
		county = "Cook"
		state = "IL"
		if rowIndex % 2 == 0:
			zipcode = "60607"
			lat = str(float(41.8781) + float((rowIndex-1) * 0.002))
			longitude = str(float(-87.6298) - float((rowIndex-1) * 0.002))
		else:
			zipcode = "60654"
			lat = str(float(41.8781) + float((rowIndex-1) * 0.0015))
			longitude = str(float(-87.6298) - float((rowIndex-1) * 0.0015))
	else:
		city = "Springfield"
		county = "Sangamon"
		state = "IL"
		zipcode = "62629"
		if rowIndex % 2 == 0:
			lat = str(float(39.7817) + float((rowIndex-1) * 0.002))
			longitude = str(float(-89.6501) - float((rowIndex-1) * 0.0015))
		else:
			lat = str(float(39.7817) - float((rowIndex-1) * 0.002))
			longitude = str(float(-89.6501) + float((rowIndex-1) * 0.0015))

	outputFile.write(indexStr)
	delimit()
	outputFile.write("Thrift Shops")
	delimit()
	outputFile.write("Resale- Second Hand- & Used Merchandise Stores")
	delimit()
	outputFile.write(name)
	delimit()
	outputFile.write(address)
	delimit()
	outputFile.write(city)
	delimit()
	outputFile.write(state)
	delimit()
	outputFile.write(zipcode)
	delimit()
	outputFile.write(phone)
	delimit()
	outputFile.write(email)
	delimit()
	outputFile.write(web)
	delimit()
	outputFile.write(lat)
	delimit()
	outputFile.write(longitude)
	delimit()
	outputFile.write(county)
	rowIndex += 1
	newLine()

