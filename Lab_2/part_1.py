from datetime import datetime

now = datetime.now()
f = now.strftime("%d/%m/%Y%H : %M : %S")

print(f"Day: {f[0:2]} \nMonth: {f[3:5]} \nYear: {f[6:10]} \nHour: {f[10:12]} \nMinute: {f[15:17]} \nSecond: {f[20:22]} ")

temp = int(input("Enter a tempature: "))

lowers = [100,80,41,10]
weather = ["Warning: Heat Wave","Hot","Normal","Cold"]
for i in range(0,len(lowers)):
    if temp < 10:
        print("The temperature you entered is out of the accepted range")
        break
    elif (temp >= lowers[i]):
        print(f"the weather at {temp} degrees fahrenheit is {weather[i]}")
        break