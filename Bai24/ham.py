def append(dsach, gtri):
  dsach += [gtri]

def insert(dsach, cso, gtri):
  if cso < 0:
    cso = 0
  elif cso > len(dsach):
    cso = len(dsach)

  return dsach[:cso] + [gtri] + dsach[cso:]

def remove(dsach, gtri):
  for i in range(len(dsach)):
    if dsach[i] == gtri:
      return dsach[:i] + dsach[i+1:]

  return dsach
