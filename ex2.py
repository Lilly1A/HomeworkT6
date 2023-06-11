"""Convertor de timp V2

Scrie un program care preia timpul introdus de utilizator în următorul format:
"11:20 PM" sau "02:00 AM".
Și îl convertește în formatul de 24 de ore.
"23:20" sau "02:00"

Combină soluția cu soluția din lecția live
și permite utilizatorului să decidă ce conversie să facă.
De la 24 de ore la 12 ore, sau invers.
"""

time=input('Introdu ora in format HH:MM ')
ora_min_list=time.split(':')
hours, minutes =int(ora_min_list[0]), int(ora_min_list[1])

if minutes > 59 or hours >=24:
    print("Ati gresit la introducere ")
elif (12<= hours <= 23) and (1<=minutes <= 59):
    hours=hours-12
    print(f'Este ora {hours}:{minutes} PM')
elif hours >= 12 and minutes == 0:
    hours=hours-12
    print(f'Este ora {hours}:{minutes} AM')
else:
    print(f'Este ora {hours}:{minutes} AM')


