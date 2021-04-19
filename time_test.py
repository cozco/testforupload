# import time

# my_time = ("28 Feb 2021")
# struct_time = time.strptime(my_time, "%d %b %Y")

# epoch_time_stamp = time.mktime(struct_time)

# print(epoch_time_stamp)

import datetime

Current_Date = datetime.datetime.today()
print ('Current Date: ' + str(Current_Date))

Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
print ('Previous Date: ' + str(Previous_Date))

NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
print ('Next Date: ' + str(NextDay_Date))

curr_in_secs = (Current_Date-datetime.datetime(1970,1,1)).total_seconds()
print(int(curr_in_secs) * 1000)