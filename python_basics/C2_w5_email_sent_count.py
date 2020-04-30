
file=open('/Users/JZ/Downloads/mbox-short.txt')


counts = dict()

for line in file:
    line=line.rstrip()
    if not line.startswith('From:'): continue
    word=line.strip().split()
    word2=word[1].split('\\')
    sender=word2[0]
    #print(sender)
    counts[sender]=counts.get(sender,0)+1
    #print(counts)


bigcount = None
bigword = None
for sender,counts in counts.items():
    if bigcount is None or counts > bigcount:
        bigword=sender
        bigcount=counts

print(bigword,bigcount)

#python downloads/py4e/C3_w5_email_sent_count.py
