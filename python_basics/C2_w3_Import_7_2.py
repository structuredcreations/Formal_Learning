#fname = input('Enter the file name:')
#fhand = open(fname)

count_a = 0
total_a = 0

fhand=open('/Users/JZ/Downloads/mbox-short.txt')

for line in fhand:
        line = line.strip()
        if line.startswith('X-DSPAM-Confidence:') :
            s = line.find('0')
            line3=line.replace('X-DSPAM-Confidence:','')
            line4=float(int(line3)
            #line2=float(line[s:6])
            #the_num=int(line[s:5])
            #count_a = count_a + 1
            #total_a = total_a + line2
            #print(line,s,the_num,count_a,total_a)
            #print(line,line3,line4)


#print("average spam confidence:",total_a/count_a)
