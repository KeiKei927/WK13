def findMaxInList(numbers):
    max_value = None
    first = True

    for num in numbers:
        if first:
            max_value = num
            first = False
        elif num > max_value:
            max_value = num
            
    return max_value

