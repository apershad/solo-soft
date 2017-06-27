# Use this function to generate a Pause part of the protocol

def pause ( file, canEndRun, autoContinue, timeToWait, message ) :
	file.write("Pause\r\n")
	file.write(message + "\r\n")
	if canEndRun:
		file.write("1\r\n")
	elif autoContinue : # canEndRun is false but autoContinue is true  
		file.write("1\r\n")
		file.write("1\r\n")
		file.write(str(timeToWait) + "\r\n")
	else : 
		file.write("0\r\n")
		file.write("0\r\n")
		file.write("\r\n")

	file.write("!@#$\r\n")

def getTip ( autoSelect = True, tipDisp = 'TipDisposal', tipLoc = 'Position3', numTips = 8 ) :
	file.write("GetTip\r\n")
	file.write(tipLoc + "\r\n")
	file.write(tipDisp + "\r\n")
	file.write(str(numTips) + "\r\n")
	if autoSelect : 
		file.write("1\r\n")
	file.write("!@#$\r\n")

fileName = raw_input("What do you want to call this protocol?")
fileName = fileName.strip() + ".hso"
file = open(fileName, 'w+')
plateLocations = "mag96_green\r\nGoldenPlate+Blue\r\nTipBox-C200uL\r\nmag96_green\r\nGoldenPlate\r\nGoldenPlate+Blue\r\n"
file.write(plateLocations)
pause ( file = file, canEndRun = False, autoContinue = True, timeToWait = 2, message = "hello")
getTip ( )



