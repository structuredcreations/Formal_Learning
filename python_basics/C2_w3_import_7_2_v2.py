#fname = input('Enter the file name:')
#fhand = open(fname)

count_a = 0
total_a = 0

fhand=open('/Users/JZ/Downloads/mbox-short.txt')

for line in fhand:
	line = line.rstrip()
	if not 'X-DSPAM-Confidence:' in line :
		continue
	count_a = count_a + 1
#	s=line.replace('X-DSPAM-Confidence:','')
#	num=float(s[:7])

	num=float(line.replace('X-DSPAM-Confidence:','')[:7])
	total_a=total_a+num

print("average spam confidence:",round(total_a/count_a,12))



    #s = line.find(':')
    #the_num=float(line[s:])
        #    count_a = count_a + 1
    #total_a = total_a + the_num
    #print(line,s,the_num,count_a,total_a)

    #print(line)


#print("average spam confidence:",total_a/count_a)
#python downloads/py4e/C2_w3_import_7_2_v2.py
