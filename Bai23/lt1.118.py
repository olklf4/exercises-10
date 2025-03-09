import ham

dso = [1,2,2,3,4,5,5]

# Câu a
dso = ham.insert(dso, 1, 1)
print('a)', dso)

# Câu b
dso = ham.insert(dso, 5, 3)
dso = ham.insert(dso, 6, 4)
print('b)', dso)
