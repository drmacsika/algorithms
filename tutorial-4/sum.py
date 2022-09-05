def total_get_sum(n: int):
    """
    Program to find the sum of all natural numbers from 1 to n.\
    Time complexity: O(n)

    n: number
    """
    sum = 0
    for i in range(n + 1):
        sum += i
    
    return sum

def total_get_sum2(n: int):
    """
    Program to find the sum of all natural numbers from 1 to n.\
    Time complexity: O(1)

    n: number
    """
    return (n * (n + 1))/2



def calc(n: int):
    sum = 0
    for i in range(n + 1):
        for j in range(i + 1):
            ...
    
    return sum


def calc(n: int):
    sum = 0
    for i in range(n + 1):
        for j in range(i + 1):
            for k in range(j + 1):
                ...
    
    return sum


# print(total_get_sum(4))