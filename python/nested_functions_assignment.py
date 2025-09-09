def calc(num):
  def fact(num):
    if num == 0:
      return 1
    return fact(num-1) * num
    
  def area(num):
    return num*num
    
  return fact(num), area(num)

n = int(input("Enter a number: "))
factorial, area = calc(n)
print("Factorial:", factorial)
print("Area:", area)
