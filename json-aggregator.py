#first argument would be the source file and the second is the target

import sys
import json

#function to calculate median value per input sensor
def Average(lst): 
    return sum(lst) / len(lst)

#function to append json values to output file
def sinkData(ouputFileHandler, outpuData):
    for x in output:
        x['median_value'] = Average(x['median_value'])
        jsonOut.write(json.dumps(x) + '\n')

#assign output file name to local variable
outputFile = sys.argv[2]

#create an empty list to store output items
output = []

#state holder to detect next date items
currentDate = None

#file handler for output file
jsonOut = open(outputFile, 'a+')

#open file handler for input file, this way it would not be loaded into memory
with open(sys.argv[1]) as jsonFile:
    #iterate throw lines of data
    for line in jsonFile:               
        source = json.loads(line)       #loads the json item as dictionary to local variable

        if source['date'] != currentDate:   #if cursor moves to the next date it should calculate mean values and flush the data into output file
            currentDate = source['date']    #set date state holder
            sinkData(jsonOut, output)
            output = []                     #free up the local variable to use for next date values

        #get the already existing sensor item for date otherwise return None
        item = next((sub for sub in output if sub['date'] == source['date'] and sub['input'] == source['input']), None)

        #if there was no record for the sensor in the current date then create one
        if item == None:
            item = {'date' : source['date'], 'input': source['input'], 'median_value': []}
            item['median_value'].append(source['value'])
            output.append(item)
        else:
            item['median_value'].append(source['value'])

#flushes the output variable one last time        
for x in output:
    x['median_value'] = Average(x['median_value'])
    jsonOut.write(json.dumps(x) + '\n')

#closes the file handler
jsonOut.close()
