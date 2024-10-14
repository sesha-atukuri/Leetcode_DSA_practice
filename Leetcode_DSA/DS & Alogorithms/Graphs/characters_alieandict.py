def find_order(words):
    """
    Args:
     words(list_str)
    Returns:
     str
    """
    # Write your code here.
    answer = ''
    for word in words:
        for ch in word:
            if ch not in answer:
                answer += ch

    return answer

print(find_order(["caa", "aaa", "aab"]))