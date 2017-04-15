# Call using;
# $ python addExifDateToFileName.py /path/to/folder

import exifread
import os
import sys

os.chdir(sys.argv[1])

fileList = os.listdir()

for fileName in fileList:
    if any(fileName[-3:] in s for s in ['JPG', "jpg", 'peg', 'img', 'IMG'] ):
        # sample names eg:
        # fileName = "DSC_0100_5.JPG"
        # fileName = "IMG_0364_3.jpg"

        # check if already processed
        if not (fileName[:2] == "20" or fileName[:2] == "19" or fileName[:1]=="_"):
            f = open(fileName, 'rb')
            tags = exifread.process_file(f)

            try:
                dateTime = "%s" % tags['EXIF DateTimeOriginal']
                dateTime =  dateTime.replace(":","")
                dateTime =  dateTime.replace(" ","_")
                dateTime += "_"
            except:
                dateTime = "_"

            newFileName = dateTime + fileName
            os.rename(fileName,newFileName)
