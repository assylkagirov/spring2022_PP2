import datetime 

today = datetime.date.today()
fivedaybefore = today - datetime.timedelta(days = 5)
print(fivedaybefore)