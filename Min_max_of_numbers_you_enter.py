def checkif_numericinput(param):
    try:
        fval = int(param)
        return fval
    except:
        print('Invalid input')

largest = None
smallest = None

while True:

    num = input("Enter an integer numer number: ")
    if num == "done":
        break
    r1 = checkif_numericinput(num)

    ###### asking for numeric input continuously if you don't enter numeric input
    while r1 is None:
        num = input("Enter an integer numer number: ")
        if num == "done":
            break
        r1 = checkif_numericinput(num)
    if num == "done":
        break
    ############################################

    if smallest is None:
        largest = r1
        smallest = r1

    if r1 < smallest:
        smallest = r1
    if r1 > largest:
        largest = r1

print("Maximum is", largest)
print("Minimum is", smallest)