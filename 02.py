secToHours = int(3600)
secondsInput = int(input("Enter seconds: "))
hours = secondsInput // secToHours
hoursMod = secondsInput % secToHours
minutes = hoursMod // 60
seconds = hoursMod % 60
print("{}:{}:{}".format(hours,minutes,seconds))