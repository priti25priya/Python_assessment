from datetime import datetime
def Calendar_Day(n):

    str_format=datetime.strptime(n,"%d %m %Y")

    cal=datetime.strftime(str_format,"%A")

    return cal