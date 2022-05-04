# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fh2=fh.read()
fh3=fh2.rstrip()
print(fh3.upper())

#or use this after fh line
#for lx in fh:
#    ly=lx.rstrip()
#    lz=ly.upper()
#    print(lz)