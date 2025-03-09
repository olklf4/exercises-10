import ham

shsinh = int(input('Nhập số học sinh: '))

if shsinh < 1:
  print('Số học sinh không hợp lệ')
else:
  dshsinh = []

  for i in range(shsinh):
    ham.append(dshsinh, input('Nhập họ tên học sinh thứ ' + str(i) + ': ').strip())

  dem = 0

  for hten in dshsinh:
    if 'HƯƠNG' in hten.split()[-1].upper():
      dem += 1

  print('Có', dem, 'bạn tên là Hương')
