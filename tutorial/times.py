from time import time, localtime, asctime

if __name__ == '__main__':
    """
    See more about time on https://www.tutorialspoint.com/python/python_date_time.htm 
    """
    ticks = time()
    print("Number of ticks since 12:00am, January 1, 1970:", ticks)

    # local time
    local_time = localtime(ticks)
    print(local_time) # time.struct_time(tm_year=2023, tm_mon=1, tm_mday=5, tm_hour=9, tm_min=50, tm_sec=51, tm_wday=3, tm_yday=5, tm_isdst=0)

    # use asctime() function to get formatted time
    formatted_time = asctime(local_time)
    print(formatted_time) # Thu Jan  5 09:52:29 2023