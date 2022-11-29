from retrieve import ReadData

rd = ReadData()

# rd.addData("1011","I am a ice cream vendor",70.655,-60.66,True)
# rd.addData("1012","I am a pani puri vendor",70.655,-60.66,True)
# rd.addData("1013","I am a handicrafts vendor",70.655,-60.66,True)


rd.registerClient("1011","Atharva","I am a handicrafts vendor",70.655,-60.66,True)
rd.registerClient("1012","Gauransh","I am panipuri vendor",70.655,-60.66,True)
rd.registerClient("1013","Aryan","I am a kitchenitem vendor",70.655,-60.66,True)
rd.getDict()

# print(rd.listRegisteredVendors())
# print(rd.getVendor('1010'))

print(rd.getLocationVendor('1011'))
