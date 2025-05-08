days = int(input("Enter the number of days to convert: "))
# convert days to seconds/minutes/hours
# 1 day = 24 hours
# 1 hour = 60 minutes
# 1 minute = 60 seconds
cal_to_seconds = 24 * 60 * 60

def unit_calculatiuon(days):
    return days * cal_to_seconds
y = days
x = unit_calculatiuon(y)
a = unit_calculatiuon(y)
print(f"{y} days = {a} minutes and {x} seconds")