#Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.


def current_recursion(current_num, n, k, current_result, final_result):

    if len(current_result) == k:
        final_result.append(list(current_result))
        return
    if current_num == n+1:
        return

    current_result.append(current_num)
    current_recursion(current_num+1, n, k, current_result, final_result)
    current_result.pop()
    current_recursion(current_num+1, n, k, current_result, final_result)


def find_combination(n,k):
    final_result = []
    current_result = []
    current_recursion(1, n, k, current_result, final_result)
    return final_result


print(find_combination(5,2))