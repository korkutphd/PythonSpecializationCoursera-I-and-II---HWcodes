def checkif_numericinput(param):
    try:
        fval = float(param)
        return fval
    except:
        print('Please enter numeric input')
        exit()
def computepay(h, r):
    h1 = checkif_numericinput(h)
    r1 = checkif_numericinput(r)
    if h1 <= 40:
        pay = h1 * r1
    else:
        pay = (h1 - 40) * (r1 * 1.5) + (40 * r1)
    return pay
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs, rate)
print("Pay", p)