import datetime

a = str(datetime.datetime.today().date())

b = f'{a[8:]}/{a[5:7]}'

print(a)