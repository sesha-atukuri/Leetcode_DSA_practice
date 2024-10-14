import heapq
from collections import Counter


def topKFrequent(nums, k):


    counter = Counter(nums)
    return heapq.nlargest(k,counter.keys(),key=counter.get)





print(topKFrequent([1,2],1))