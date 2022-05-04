# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
value_f_total = 0
count2 = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    count = 1
    sp1 = line.find(':')
    while line[sp1 + count] == ':':
        count = count + 1

    value = line[sp1 + count:len(line)]
    value_f = float(value)
    count2 = count2 + 1
    value_f_total = value_f_total + value_f

avg = value_f_total / count2

print('Average spam probability: ',avg)

