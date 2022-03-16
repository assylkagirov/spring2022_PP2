date1 = input().split('-')
date2 = input().split('-')
print(str((int(date1[2]) * 365 + int(date1[1]) * 30 + int(date1[0])) * 86400 - (int(date2[2]) * 365 + int(date2[1]) * 30 + int(date2[0])) * 86400))