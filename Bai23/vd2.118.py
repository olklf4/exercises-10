sluong = int(input('Nhập số lượng: '))
dso = [0, 1]

for i in range(min(sluong + 1, 2)):
  print(dso[i])

if sluong > 1:
  for i in range(2, sluong):
    fib = sum(dso)
    dso[0] = dso[1]
    dso[1] = fib
    print(fib)
