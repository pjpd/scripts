import csv
import os
import shutil
import xml.etree.ElementTree as etree



TEAMS_CSV_PATH = "arkTeams.csv"
TRACKS_CSV_PATH = "arkPaths.csv"
SAMPLE_KML_PATH = "SampleKmlFile.kml"


def listFromCsvFile(fileName):
	csvList = list( csv.reader( open( "./" + fileName ) ) )
	return csvList

coordinateList = listFromCsvFile(TRACKS_CSV_PATH)
boatList = listFromCsvFile(TEAMS_CSV_PATH)

pathName = "ARC+2016"

for boat in boatList[1:]:
	boatId = boat[2]
	boatName = boat[3]
	country = boat[1]
	boatType = boat[5]
	documentName = boatName + "_" + country + "_" + boatType

	with open ("SampleKmlFile.kml", "r") as kmlFile:
		kmlString = kmlFile.read()


	boatCoordinates = ""
	for coordinate in coordinateList:
		if coordinate[0] == boatId:
			boatCoordinates+=coordinate[2] + "," + coordinate[3] + ",0 "


	kmlString = kmlString.replace("DocumentName", documentName)
	kmlString = kmlString.replace("PathName", pathName)
	kmlString = kmlString.replace("KmlCoordinates", boatCoordinates)


	with open(pathName + "_" + documentName + ".kml", "w") as text_file:
	    text_file.write(kmlString)
