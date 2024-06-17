def perimeter(length, breadth):
  p = 2 * (length + breadth)
  return p

def area(length, breadth):
  a = length * breadth
  return a


l = int(input('enter the length: '))
b = int(input('enter the breadth: '))

print(perimeter(l, b))
print(area(l, b))