def mergeintervals(intervals):

    intervals.sort(key=lambda x:x[0])
    output = []

    for interval in intervals:
        if not output or output[-1][1] < interval[0]:
            output.append(interval)
        else:
            output[-1][1] = max(output[-1][1], interval[1])

    return output


print(mergeintervals([[1,3],[2,6],[8,10],[15,18]]))