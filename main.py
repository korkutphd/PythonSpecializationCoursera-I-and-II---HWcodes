fname = input("Enter file name: ")

fhand=open(fname)

count=0;
for line in fhand:
    line2 = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    print(words[1])
    count=count+1;

print('There were',count,'lines in the file with From as the first word')

