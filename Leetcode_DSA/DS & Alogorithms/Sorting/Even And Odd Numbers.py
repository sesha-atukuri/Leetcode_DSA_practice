def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    for num in range(len(numbers)//2):
        if numbers[num]%2 != 0:
            if numbers[len(numbers)-1-num]%2 == 0:
                numbers[num], numbers[len(numbers)-1-num] = numbers[len(numbers)-1-num], numbers[num]

    return numbers

print(segregate_evens_and_odds([1, 2, 3, 4]))