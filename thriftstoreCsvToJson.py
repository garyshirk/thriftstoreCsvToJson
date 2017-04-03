import csv
import sys

def newLineAndTab(outputFile, numTabs):
	outputFile.write("\n")
	for num in range(0, numTabs - 1):
		outputFile.write("\t")
	outputFile.write("END TAB")

def outputLineFor(outputFile, header, row, col):
	colnum = 0
	for col in row:
		outputFile.write("\"" + header[colnum] + "\": {")
		print header[colnum], col
		colnum += 1

def parseCsvToJson(outputFile):
	currentState = ""
	currentCounty = ""
	with open('Thrift_Shops_Sample_Test.csv', 'rb') as f:
		reader = csv.reader(f, delimiter=';')
		rownum = 0
		for row in reader:
			if rownum == 0:
				header = row
			else:
				colnum = 0
				for col in row:
					if colnum == 6:
						rowState = col
						if currentState != rowState:
							currentState = rowState
							outputFile.write("\"" + currentState + "\": {")
							newLineAndTab(outputFile, 3)
							print "write new state: " + currentState
					if colnum == 13:
						rowCounty = col
						if currentCounty != rowCounty:
							currentCounty = rowCounty
							outputFile.write("\"" + currentCounty + "\": {")
							newLineAndTab(outputFile, 4)
							print "write new county: " + currentCounty
					colnum += 1
				colnum = 0
				outputLineFor(outputFile, header, row, col)
			rownum += 1
	f.close()

# Open output file
outputFile = open('thriftstores.json', 'w')

# {
#	thriftstores: {
outputFile.write("{\n\t\"thriftstores:\"  {")
newLineAndTab(outputFile, 2)

# Convert csv to json
parseCsvToJson(outputFile)

#	}
#}
newLineAndTab(outputFile, 1)
outputFile.write("}\n")
newLineAndTab(outputFile, 0)
outputFile.write("}\n")

# Close output file
outputFile.close()

