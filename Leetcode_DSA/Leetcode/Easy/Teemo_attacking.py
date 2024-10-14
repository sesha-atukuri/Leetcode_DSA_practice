
def findPoisonedDuration(timeSeries, duration):

    total_sec = 0
    for time in timeSeries:
        #if time
        end_sec = time+duration-1
        if end_sec >
        total_sec += duration


    return total_sec

print(findPoisonedDuration([1,4],2))


