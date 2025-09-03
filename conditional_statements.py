age = int(input("Enter your age: "))
income = int(input("Enter your income: "))
credit_score = int(input("What's your credit score: "))

if age > 21 or income > 25000 or credit_score > 650:
  print("Loan Approved!")
else:
  print("Not Eligible!")

# ---------------------------------------------------------------------

s1 = int(input("Enter marks in subject 1: "))
s2 = int(input("Enter marks in subject 2: "))
s3 = int(input("Enter marks in subject 3: "))

if s1 > 40 and s2 > 40 and s3 > 40 and (s1 + s2 + s3) / 3 > 50:
  print("Passed!")
else:
  print("Failed!")
