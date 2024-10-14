def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    i = 0
    j = len(numbers) - 1
    while i <= j:
        if numbers[i] % 2 == 0:
            i += 1
        else:
            if numbers[j] % 2 == 0:
                numbers[i], numbers[j] = numbers[j], numbers[i]
            else:
                j -= 1

    return numbers

print(segregate_evens_and_odds([1, 2, 3, 4]))