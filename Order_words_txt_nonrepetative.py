fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    vars_in_var = line.split()
    for x in range(len(vars_in_var)):
        if vars_in_var[x] not in lst:
            lst.append(vars_in_var[x])

lst.sort()
print(lst)
