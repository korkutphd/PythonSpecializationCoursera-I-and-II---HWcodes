fname = input("Enter file name: ")

fhand=open(fname)

counts=dict()
count=0

for line in fhand:
    line2 = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    counts[words[1]]=counts.get(words[1],0)+1

print(counts)

bigcount=None
bigword=None
for word, count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)


