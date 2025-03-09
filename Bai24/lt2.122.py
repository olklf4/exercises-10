import string

cs = list(string.ascii_letters + string.digits)
xau = input('Nhập xâu S: ')
ktra = False

for ktu in xau:
  if ktu in cs:
    ktra = True
    break

if ktra:
  print('S có chứa chữ số')
else:
  print('S không chứa chữ số nào')
