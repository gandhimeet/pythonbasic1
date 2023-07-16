'''
Write a Python program to convert all units of time into seconds.
'''
#input of days hours minutes seconds
days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))
#time w.r.t days hours minutes seconds
time = days + hours + minutes + seconds
#displaying output
print("The  amounts of seconds", time)
