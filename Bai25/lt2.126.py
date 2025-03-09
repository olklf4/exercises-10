hten = input('Nhập họ và tên: ').strip().split()
print('Tên: ', hten[-1])

if len(hten) > 1:
  print('Họ đệm', hten[1])