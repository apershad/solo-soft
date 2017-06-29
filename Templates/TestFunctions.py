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

# Use this function to grab Tips from the Tip Box

def getTip ( file, autoSelect = True, tipDisp = 'TipDisposal', tipLoc = 'Position3', numTips = 8 ) :
    file.write("GetTip\r\n")
    file.write(tipLoc + "\r\n")
    file.write(tipDisp + "\r\n")
    file.write(str(numTips) + "\r\n")
    if autoSelect : 
        file.write("1\r\n")
    file.write("!@#$\r\n")

def loop ( file, iter ) :
    file.write("Loop\r\n")
    file.write(str(iter) + "\r\n")
    file.write("!@#$\r\n")

def endLoop ( file ):
    file.write("EndLoop\r\n!@#$\r\n")

def setSpeed ( file, speed = 100 ) :
    file.write (str(speed) +"\r\n!@#$\r\n")

def shuckTip (file, tipDisp = 'TipDisposal') :
    file.write("ShuckTip\r\n")
    file.write(tipDisp + "\r\n!@#$\r\n")

# def dispense ( file, speed, backlash, blow_off, namedPos = [True, beads, 80], mixing = [0, 0, 0, 0, 0, 0], rowOrCol = [True, False], shift = [0, 0, 0, 0, 0, 0, 0])
# file 
# named or plate
    # if named ask for named point, dispense vol
    # if plate ask for plate loc, ask for a plate typed out, ask for # of dispenses to perform on each pass
# syringe speed
# backlash
# blow-off
# shifts = [XShift, YShift, ZShift, DoTipTouch?, Tip Touch]
# roworcol = [isRow, isReverse]
# mixing = [mix at finish, mix cycles, mix vol, asp height, delay, dwell]
#def dispense ( file, isPlate, platePos, plate, rowOrCol, param) : # speed, backlash, blow_off, shift, rowOrCol, mixing ) :
#   file.write("Dispense\r\n")
#   if named :
#       file.write("")
#       pointName = raw_input("Name the exact point to dispense to. ")
#       vol = raw_input("What's the volume to dispense? ")
#   else :
#       print (plateLocations)
#       position = "Position" + raw_input("Please Enter the line number of the plate you want. Also keep in account how many plate locations your Hudson has. ");

# dispense will write the protocol to dispense to a specific point
    # file = spec file
    # loc = String containing loc name (case/style is very important)
        # that's either plate position (Position1....Position6 etc)
        # OR named point like Beads, 500uL Eppindorf, etc. 
    # vol = dispense volume
        # either 96 well plate in the form [[],[],[],etc] where each inner list is a row
            # represent each row as 0,0,0,0,0,0,0,0,0,0,0,0
            # replace the 0's with whatever you watn the dispense volume to be
        # OR just a single integer representing volume
    # param = LIST detailing following information in this order:
        # Syringe-Speed = this is a % value between 0 and a 100 
        # Backlash = an integer representing a uL backlash value
        # Blow-off = an integer representing a uL blow-off value
    # shift = [X Shift, Y shit, Z shift, doTipTouch, X Tip Touch Shift, Y Tip Touch Shift, Z Tip Touch Shift]
        # X shift, Y Shift, Z shift - integer value mm
        # doTipTouch = 0 (NO) or 1 (YES)
        # X Tip Touch Shift, Y Tip Touch Shift, Z Tip Touch Shift - integer value mm
def dispense (file, vol, loc, param, mix, order, shift) :
    file.write ("Dispense\r\n")
    plate = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
    if not (isinstance( vol, int)) :
        isPlate = True
        plate = vol
        point = loc
        file.write(point + "\r\n")
        file.write("\r\n")
    else :
        isPlate = False
        point = loc
        file.write("\r\n")
        file.write(str(vol) + "\r\n")
    file.write(str(2) + "\r\n")
    file.write(str(param[0]) + "\r\n")
    file.write(str(param[1]) + "\r\n")
    file.write(str(isPlate) + "\r\n")
    file.write(str(not isPlate) + "\r\n")
    isRow = order[0]
    file.write(str(isRow) + "\r\n")yg
    file.write(str(not isRow) + "\r\n")
    file.write(point + "\r\n")
    for i in range(0,7) :
        file.write(str(shift[i]) + "\r\n")
    file.write("\r\n")
    file.write(str(1) + "\r\n")
    file.write(str(mix[5]) + "\r\n")
    file.write(str(param[2]) + "\r\n")
    for i in range (0, 5) :
        file.write(str(mix[i]) + "\r\n")
        if i == 2 :
            file.write("a\r\n")
    for i in range(0,8) :
        file.write(",".join(str(j) for j in plate[i]))
        file.write("\r\n")
    file.write(str(order[1]) + "\r\n!@#$\r\n")

def aspirate (file, vol, loc, param, mix, order, shift)
file = open("GetDispenseShuck.hso", 'w+')
plateLocations = "mag96_green\r\nGoldenPlate+Blue\r\nTipBox-C200uL\r\nmag96_green\r\nGoldenPlate\r\nGoldenPlate+Blue\r\n"
file.write(plateLocations)
pause ( file = file, canEndRun = False, autoContinue = True, timeToWait = 2, message = "hello")
loop ( file = file, iter = 4 )
getTip ( file = file )
dispense( file = file, vol = 4, loc = "Position1", param = [3,3,3], mix = [0,0,0,0,0,0], order = [True, 0], shift = [0,0,0,0,0,0,0])
shuckTip (file = file )
endLoop ( file = file )


