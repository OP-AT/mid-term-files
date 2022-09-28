# Write a Python function/method SwapMiddle(Codes) to swap the first half of the
# content of the list Codes with second half of the list Codes and display the swapped
# values. For e.g. if the list Codes contains : [22,44,55,66,88,11] then function should
# swap and display as: [66,88,11,22,44,55]

def SwapMiddle(lst):
    for a in lst[5:2:-1]:
        lst.insert(0, a)
        lst.pop()
    return lst





lst = [22, 44, 55, 66, 88, 11]
print(SwapMiddle(lst))