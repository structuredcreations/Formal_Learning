
file=open('/Users/JZ/Downloads/romeo.txt','r')
text = file.read()
file.close()

all_words = list(text.split())

#create a list of unique text_words

unique_words = list()

for word in all_words :
    if word not in unique_words:
        unique_words.append(word)
unique_words.sort()

print(unique_words)


#for word in text_words :
#    if word not in text_words:
#        list.append()
#print(words)


#words = list()
#words.append()

#words = list(text.split())

#print(words)
