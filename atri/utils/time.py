import time

microsecond = 1
second = 1000 * microsecond
minute = 60 * second
hour = 60 * minute
day = 24 * hour

def now() -> int:
    return time.time_ns()//1000
