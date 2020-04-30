
import re

running_sum = 0

#file=open('/Users/JZ/Downloads/regex_sum_42.txt')
file=open('/Users/JZ/Downloads/regex_sum_351799.txt')

numlist=list()


for line in file:
    line=line.rstrip()
    num_text=re.findall('[0-9]+',line)
    for num_int in num_text :
        num_int = float(int(num_int))
        running_sum = running_sum + num_int
        print(num_int,running_sum)


print('total is',running_sum)
#330686

#python downloads/py4e/C3_w2_extract_count_number.py
