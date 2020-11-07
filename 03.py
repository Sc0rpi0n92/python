seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
seasons_list = ['winter', 'spring', 'summer', 'autumn']
while True:
    month = input("Enter number of month: ") #input check
    if month.isdigit():
        month = int(month) #str to int
        break
if month ==1 or month == 12 or month == 2:
    print("By dictionary: ",seasons_dict.get(1))
    print("By list: ",seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print("By dictionary: ",seasons_dict.get(2))
    print("By list: ",seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print("By dictionary: ",seasons_dict.get(3))
    print("By list: ",seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print("By dictionary: ",seasons_dict.get(4))
    print("By list: ",seasons_list[3])
else:
    print("ERROR 404. This month is not found")
