num = 1
 
while num < 1:
    print("The number is ", num)
    num += 1
   
   
print( "below is the do while loop")
while True:
    print("The number is ", num)
    num += 1
   
    if num > 1:
        break
   
print("below is the range")
for i in range(2,10):
    if i==5:
        print(" breaking the loop ", i)
        continue
    print("The number is ", i)
