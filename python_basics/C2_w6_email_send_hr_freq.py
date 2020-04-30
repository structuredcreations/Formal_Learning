file=open('/Users/JZ/Downloads/mbox-short.txt')

counts = dict()

for line in file:
    line=line.rstrip()
    if not line.startswith('From '): continue
    word=line.split()
    time=word[5].split(':')
    hour=time[0]
    #print(hour)
    counts[hour]=counts.get(hour,0)+1

lst=list()
for key, val in counts.items():
    newtup = (key,val)
    lst.append(newtup)

lst = sorted(lst)

for val,key in lst[:]:
    print(val,key)
