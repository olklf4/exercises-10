import ham

dai = int(input('Nhập độ dài dãy: '))

if dai < 1:
  print('Độ dài không hợp lệ')
else:
  dso = []

  for i in range(1, dai + 1):
    ham.append(dso, float(input('Nhập giá trị thứ ' + str(i) + ': ')))

  csgiua = dai // 2
  del dso[csgiua]

  if len(dso) % 2 != 0:
    del dso[csgiua - 1]

  print(dso)
