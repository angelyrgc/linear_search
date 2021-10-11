def recursive_binary_search(list,target):
    "Returns true or false, depending if the target exists or not"

    "Considering whats happens  if an empty list is passed in, in that case it will return false"
    if len(list) == 0: 
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint +1:],target)
            else:
                return recursive_binary_search(list[: midpoint], target)

def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]
result=recursive_binary_search(numbers,12)
verify(result)

result = result = recursive_binary_search(numbers,6)
verify(result)