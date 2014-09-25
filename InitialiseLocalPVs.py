from org.csstudio.opibuilder.scriptUtil import PVUtil
# This is rather fragile : the input arguments to the script have to be correctly 
# defined in the attributes of the script as attached to some widget.
# Get access to pvs[0] == loc://speedA
speedAname = PVUtil.getString(pvs[0])
speedApv = PVFactory.createPV(speedAname)
speedApv.start()
speedApv.setValue(50)
# Get acces to pvs[1] == loc://speedB
