#Task 1
#The point of this function/task is to have a list of elements which would then be sublisted into groups of 3.
#Any remained elements will be put into a sublist together, even if there is no second or third. The input of
#this is a list of integers, and the output is a list of lists. Each list within the list will have 3 integers
#and any leftover will be put into its own list, as previously stated.

def groups_of_3(values: list[int]) -> list[list[int]]:
    lastList = []
    end = ((len(values)//3)*3)
    for x in range(0, end, 3):
        newList = []
        for y in range(x, x+3):
            newList.append(values[y])
        lastList.append(newList)
    newList = []
    if end < len(values):
        for x in range(end, len(values)):
            newList.append(values[x])
        lastList.append(newList)
    return lastList