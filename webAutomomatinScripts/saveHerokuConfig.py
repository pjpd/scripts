# Gets a list of apps on a heroku account
# Returns all heroku_applicaton variables for those accounts
# 2015-01-08 Updated to work on python 3.5.0

import os
from datetime import datetime
import csv
import copy


heroku_applicatons = os.popen("heroku apps").read().split("\n")
heroku_applicatons.pop(0)

keys = ["keys"]
for heroku_applicaton in heroku_applicatons:
    keys.append(heroku_applicaton)
table = [keys]

col = 1
emptyRow = [None]*(len(heroku_applicatons)+1)
while(heroku_applicatons):
    heroku_applicaton = heroku_applicatons.pop(0)
    if(heroku_applicaton == ""):
        continue
    print("heroku config -a " + heroku_applicaton)

    application_variables = os.popen("heroku config -a " + heroku_applicaton).read().split("\n")
    for application_variable in application_variables:
        arr = application_variable.split(": ")
        if len(arr) == 2:
            key = arr[0].strip()
            value = arr[1].strip()
            foundRow = False
            for i in range(1, len(table)-1):
                row = copy.copy(table[i])
                if row[0] == key:
                    row[col] = value
                    table[i] = copy.copy(row)
                    foundRow = True
            if not foundRow:
                row = copy.copy(emptyRow)
                row[0] = key
                row[col] = value
                table.append(copy.copy(row))
        elif((arr[0][:3] == "===") | (arr[0][:3] == "")):
            continue
        else:
            print("line wrong length")
            print(arr)
    col+=1

# Write csv
d = datetime.now()
currentDateTime = d.strftime('%Y%m%d_%H%M%S')
pDir = os.path.dirname(os.path.abspath(__file__)) + '/ConfigVars'
print(pDir)
if not os.path.exists(pDir):
    os.makedirs(pDir)


with open(pDir + '/reassure_config_' + currentDateTime + '.csv', "w") as f:
    writer = csv.writer(f)
    writer.writerows(table)

print("Finished!")
