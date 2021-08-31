import datetime
mytime = datetime.time(hour=2,minute=20)
print(mytime.minute)
print(mytime)
date=datetime.date.today()
print(date)


from datetime import date
date1 = date(2021,11,3)
date2 = date(2020,11,3)
result = date1 - date2
print(result)


