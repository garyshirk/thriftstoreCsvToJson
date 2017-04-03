import csv
import sys

ID_COL = 0
STATE_COL = 6
LAT_COL = 11
LONG_COL = 12
COUNTY_COL = 13

def newLineAndTab(outputFile, numTabs):
	outputFile.write("\n")
	for num in range(0, numTabs):
		outputFile.write("\t")

def outputStoreDataFor(outputFile, header, row, col):
	colnum = 0
	for col in row:
		if colnum == 0:
			newLineAndTab(outputFile, 4)
			outputFile.write("\"" + col + "\": {")
		newLineAndTab(outputFile, 5)
		if colnum == ID_COL or colnum == LAT_COL or colnum == LONG_COL:
			outputFile.write("\"" + header[colnum] + "\": " + col + ",")
		elif colnum == COUNTY_COL:
			outputFile.write("\"" + header[colnum] + "\": " + "\"" + col + "\"")
		else:
			outputFile.write("\"" + header[colnum] + "\": " + "\"" + col + "\",")
		colnum += 1
	# Close the current row
	newLineAndTab(outputFile, 4)
	outputFile.write("}")

def parseCsvToJson(outputFile):
	currentState = ""
	currentCounty = ""
	with open('Thrift_Shops_Sample_Test.csv', 'rb') as readFile:
		reader = csv.reader(readFile, delimiter=';')
		rownum = 0
		for row in reader:
			if rownum == 0:
				header = row
			else:
				colnum = 0
				stateChanged = False
				for col in row:
					if colnum == STATE_COL:
						rowState = col
						if currentState != rowState:
							stateChanged = True
							# Don't close state if this is very first time through loop
							if currentState != "":
								# Close the county
								newLineAndTab(outputFile, 3)
								outputFile.write("}")
								# Close the state
								newLineAndTab(outputFile, 2)
								outputFile.write("},")
							currentState = rowState
							newLineAndTab(outputFile, 2)
							outputFile.write("\"" + currentState + "\": {")
					if colnum == COUNTY_COL:
						rowCounty = col
						if currentCounty != rowCounty:
							# Close the county only if state did not change,
							# otherwise country already got closed above
							if stateChanged == False:
								newLineAndTab(outputFile, 3)
								outputFile.write("},")
							currentCounty = rowCounty
							newLineAndTab(outputFile, 3)
							outputFile.write("\"" + currentCounty.lower() + "\": {")
						else:
							# Since county didn't change, need "," before next store is added
							outputFile.write(",")
					colnum += 1
				colnum = 0
				outputStoreDataFor(outputFile, header, row, col)
			rownum += 1
	readFile.close()

# Open output file
outputFile = open('thriftstores.json', 'w')

# {
#	thriftstores: {
outputFile.write("{")
newLineAndTab(outputFile, 1)
outputFile.write("\"thriftstores\":  {")

# Convert csv to json
parseCsvToJson(outputFile)

# Close the last county
newLineAndTab(outputFile, 3)
outputFile.write("}")

# Close the last state
newLineAndTab(outputFile, 2)
outputFile.write("}")

# Close "thriftstores"
newLineAndTab(outputFile, 1)
outputFile.write("}")

# Close the overall json file
newLineAndTab(outputFile, 0)
outputFile.write("}\n")

# Close output file
outputFile.close()

