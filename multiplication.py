#multiplication table from 1 to 12
num = 5
num = int(input("show the multiplication table of? "))
#iterate 12 times from i = 1 to i = 13
for i in range(1, 13):
    print(num, 'x', i, '=', num*i)
