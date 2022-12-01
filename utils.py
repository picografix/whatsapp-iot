"""
User commands:
- bot show vendors
- bot show "id"
- bot location id
- bot register id
- bot nearby vendors

"""

def extractCommand(msg):
    # msg = msg.split(" ")
    if(msg[0]=="bot"):
        if(msg[1]=="show" and msg[2]=="vendors"):
            return 1
        elif(msg[1]=="show"):
            return 2
        elif(msg[1]=="location"):
            return 3
        elif(msg[1]=="register"):
            return 4
        elif(msg[1]=="nearby"):
            return 5
        else:
            return 0
    else:
        return 0


help_msg = "The bot only works for the following commands \n"
help_msg+= "1. Bot show vendors: To get a list of vendors \n"
help_msg+= "2. Bot show vendors_name : To get a detailed description of the vendor \n"
help_msg+= "3. Bot location vendor_name: Get the current location of the vendor \n"
help_msg+= "4. Bot register vendor_name: Register vendor for nearby alert \n"
help_msg+= "5. Bot nearby vendors: To get a list of vendors nearby "


# print(extractCommand("bot show there"))
