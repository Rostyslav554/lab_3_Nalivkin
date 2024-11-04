hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins_1 = mins + dura
hour_2 = hour + mins_1 // 60
mins_1 = mins_1 % 60
hour_2 = hour_2 % 24
print("Event will end at : ",hour_2, ":",mins_1)