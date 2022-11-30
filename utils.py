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


# print(extractCommand("bot show there"))
