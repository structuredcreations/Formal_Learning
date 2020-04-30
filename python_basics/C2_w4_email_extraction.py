
file=open('/Users/JZ/Downloads/mbox-short.txt')

count_a = 0

for line in file:
    line=line.rstrip()
    if not line.startswith('From:'): continue
    word=line.strip().split()
    word2=word[1].split('\\')
    print(word2[0])
    count_a = count_a + 1


print("There were",count_a,"lines in the file with From as the first word")

#python3 downloads/py4e/C2_w4_email_extraction.py
