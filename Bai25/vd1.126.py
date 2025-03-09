tnhien = input('Nhập 2 số tự nhiên: ').strip().split()
if len(tnhien) != 2:
  print('2 số tự nhiên không hợp lệ')
else:
  tn1, tn2 = int(tnhien[0]), int(tnhien[1])

  while tn2:
    tn1, tn2 = tn2, tn1 % tn2

  print('Ước chung lớn nhất là', tn1)
