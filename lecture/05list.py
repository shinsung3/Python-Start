"""
list
"""
    #  [0 1 2 3 4 5]
list = [1,2,3,4,5,6]
# index를 가지고 있다
# 순서가 있다
# {a, b, c}
# {b, c, a}
# {b, a, c}
print(list)
print(list[0])
print(list[5])
print(list[-3])
list[0] = 10
print(list)
# print(list[6]) # runtime error
# print(list2[3]) # compile error