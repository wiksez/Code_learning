def minimal(nums):
    minElement = 1000
    for v in nums.values():
        if v < minElement:
            minElement = v

    return minElement


data1 = dict(x=5, y=8, z=7, a=1, b=20)
data2 = dict(x=5, y=8, z=-7, a=1, b=20)

min1 = minimal(data1)
min2 = minimal(data2)

if min1 < min2: 
    print(min1)
else:
    print(min2)