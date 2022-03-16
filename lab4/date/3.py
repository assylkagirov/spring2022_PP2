import datetime 

today = datetime.datetime.now()
dropmicrosec = datetime.datetime.today().replace(microsecond=0)
print(dropmicrosec)