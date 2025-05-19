import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today() # using the .today() method to get the current date

time = datetime.time(12, 30, 0)
now = datetime.datetime.now() # using the .now() method to get current time on our system

now =now.strftime("%H:%M:%S %d-%m-%Y") #using the strftime() method to format our date to a choice



###lets create a game to check if a target date has passed

target_datetime = datetime.datetime(2020, 1, 2, 12, 30, 1)

current_datetime = datetime.datetime.now()


if target_datetime < current_datetime:
    print("Target date passed")
else:
    print("targat date has not passed")