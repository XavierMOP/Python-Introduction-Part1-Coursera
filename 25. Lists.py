# Create

my_list = []
print(my_list)

L1 = ['qwe', 'rty', 'uio', 'zxc']
print(L1)

L2 = [1, 52, 36, -56, 90]
print(type(L2))
print(type(L2[0]))
print(L2)

L3 = [[3, 4], ['a', 'b', 'c'], []]
print(L3)

# Access

print(len(my_list), len(L1), len(L2), len(L3))

print('first element:', L1[0])
print('last element:', L1[-1])
print(L3[1])
print(L2[1:3])

# Update

L1[0] = 'NEW'
print(L1)
