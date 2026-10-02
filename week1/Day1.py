"""def analyze_number(num):
    if not num:
        return {"Largest": None, "Smallest": None, "Average": None}

    l = max(num)
    s = min(num)
    a = sum(num) / len(num)
    return {"Largest": l, "Smallest": s, "Average": a}
nums = [10, 20, 30, 40, 50]
result = analyze_number(nums)
print(result)"""
# *********************************************************************************
# *********************************************************************************
"""def analyze_number(num):
    if not num:
        return {"Largest": None, "Smallest": None, "Average": None}
    largest = num[0]
    smallest = num[0]
    sum = 0
    cnt = 0

    for n in num:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
        sum += n
        cnt += 1
    avg = sum/cnt
    return {"Largest": largest, "Smallest": smallest, "Average": avg}
nums = [10, 20, 30, 40, 50]
result = analyze_number(nums)
print(result)"""

# *********************************************************************************
# *********************************************************************************

# Normal function
"""from functools import reduce


def add(a, b):
    return a + b

# Same thing as a lambda
add = lambda a, b: a + b
print(add(2, 3))  # 5

#map()
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8, 10]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

total = reduce(lambda x, y: x + y, nums)
print(total)  # 15

words = ["banana", "kiwi", "apple", "fig"]
print(sorted(words, key=lambda w: len(w)))

people = [{"name": "Asha", "age": 25}, {"name": "Ravi", "age": 17}, {"name": "Meera", "age": 30}]
print(list(map(lambda p: p["name"], filter(lambda p: p["age"] >= 18, people))))"""

from functools import reduce
numbers = [4, 11, 7, 20, 3, 15]
words = ["banana", "kiwi", "apple", "fig"]
print(list(map(lambda x: x * 2, numbers)))

print(list(filter(lambda x: x > 4, numbers)))

print(reduce(lambda x, y: x * y, numbers))

print(reduce(lambda x, y: x if x>y else y, numbers ))

print(list(map(lambda w: w.upper(), words)))

print(list(sorted(words, key=lambda w: w[-1])))