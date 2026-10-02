#user input times in mins
swimming_time = int(input("swimming time (mins) = "))
cycling_time = int(input("cycling time (mins) = "))
running_time = int(input("running time (mins) = "))

total_time = swimming_time + cycling_time + running_time

if total_time < 100:
    print("Award: Provincial colours")
elif total_time >= 101 and total_time <= 105:
    print("Award: Provincial half colours")
elif total_time >= 106 and total_time <= 110:
    print("Award: Provincial scroll")
else:
    print("No Award")