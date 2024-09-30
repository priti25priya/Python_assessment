from datetime import datetime
def Time_delta():

    timestamp1 = "2021-10-23 15:00:00 +0530"
    timestamp2 = "2021-10-23 07:30:00 +0000"


    time1 = datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S %z")
    time2 = datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S %z")

    time_difference = abs(time1 - time2)


    return time_difference