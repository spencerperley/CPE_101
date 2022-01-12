from datetime import datetime

now = datetime.now()
f = now.strftime("%d/%m/%Y%H : %M : %S")

print(f"Day: {f[0:2]} \nMonth: {f[3:5]} \nYear: {f[6:10]} \nHour: {f[10:12]} \nMinute: {f[15:17]} \nSecond: {f[20:22]} ")





