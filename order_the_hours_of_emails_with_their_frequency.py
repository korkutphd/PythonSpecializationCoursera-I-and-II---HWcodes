fname = input("Enter file name: ")

fhand=open(fname)

counts=dict()
count=0

for line in fhand:
    line2 = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        allwords=words[5]
        hour=allwords.split(':')

        counts[hour[0]]=counts.get(hour[0],0)+1

thetups=sorted([(k,v) for k,v in counts.items()])

for aa,bb in thetups:
    print(aa,bb)



