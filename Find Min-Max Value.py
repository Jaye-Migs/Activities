#Min_Max Value

ramGhz=[1200, 2400, 2666, 3200]

print(max(ramGhz))
print(min(ramGhz))

def ramGhzCustom(iterable):
     minimum = iterable[0]
     for value in iterable[1:]:
         if value < minimum:
             minimum = value
     return minimum

print(ramGhzCustom(ramGhz))