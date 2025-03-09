import ham

shsinh = int(input('Nhập số học sinh: '))

if shsinh < 1:
  print('Số học sinh không hợp lệ')
else:
  dshsinh = []

  for i in range(shsinh):
    ham.append(dshsinh, input('Nhập họ tên học sinh thứ ' + str(i) + ': ').strip())

  tim = input('Nhập tên học sinh cần tìm: ').upper()

  dem = 0

  for hten in dshsinh:
    if tim in hten.split()[-1].upper():
      dem += 1

  print('Có', dem, 'bạn cùng tên')