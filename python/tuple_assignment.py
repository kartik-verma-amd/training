product = "Laptop", 50000, "Black", "Samsung", "Electronics"
print(product)

print(product[1])

print(product[len(product)-2:])

for i in range(len(product)):
  if product[i] == "Electronics":
    print("Electronics is present in the tuple")
    break
else:
  print("Electronics isn't present in the tuple")

prod_prices = 1000, 1500, 1200, 1100, 900

cnt = 0
for i in range(len(prod_prices)):
  if prod_prices[i] == 1000:
    cnt += 1

print("1000 appears", cnt, "times")

if len(prod_prices) > 0:
  min = max = prod_prices[0]
for i in range(len(prod_prices)):
  if prod_prices[i] > max:
    max = prod_prices[i]
  elif prod_prices[i] < min:
    min = prod_prices[i]

for i in product:
  print(i)

lst_prod = list(product)
lst_prod[1] = 55000
updated_prod = tuple(lst_prod)
print(updated_prod)

concat_prod = updated_prod + ("In Stock",)
print(concat_prod)

lst_p2 = list(concat_prod)
lst_p2.remove("Electronics")
updated_p2 = tuple(lst_p2)
print(updated_p2)

a, b, c, *rest = updated_p2
print(a, b, c, sep='\n')

nested_prod = (updated_p2,) * 3
print(nested_prod[1])
