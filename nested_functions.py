def calcualte(num1, num2):
   
    def cube(a):            # nested function 1
        return a*a*a
   
    def square(a):          # nested function 2
        return a*a
   
    res1 = cube(num1)
    res2 = square(num2)
 
    return res1, res2      # tuple from here  (res1,res2)
 
a = int(input(" enter first number "))
b = int(input(" enter second number "))
 
m,n = calcualte(a,b)    # unoacking of the tuple values
print(" cube is ", m)
print(" square is ", n)
