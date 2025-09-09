with open("file.txt", "w+") as file:
    file.write("abc\n")
    file.write("def\n")
    file.write("ghi\n")
    file.write("jkl\n")
    file.write("mno\n")
    file.write("pqr\n")
    file.write("stu\n")
    file.write("vwx\n")
    file.write("yz\n")
    file.seek(0)
    lines = file.readlines()
    print(lines)


with open("odd.txt", "w+") as odd_file:
    for i in range(0, len(lines), 2):
        odd_file.write(lines[i])
        
    odd_file.seek(0)
    print(odd_file.read())

with open("even.txt", "w+") as even_file:
    for i in range(1, len(lines), 2):
        even_file.write(lines[i])
        
    even_file.seek(0)
    print(even_file.read())
