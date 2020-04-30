largest_so_far = -1
count_a = 0
total_a = 0

print('before',largest_so_far)
for the_num in [9,41,12,3,74,15] :

# this is the first section of finding the max
    if the_num > largest_so_far :
        largest_so_far=the_num
    print(largest_so_far,the_num)

    count_a = count_a + 1
    total_a=total_a + the_num


print('After max',largest_so_far)
print('After count',count_a)
print('After total',total_a)
print('After average',total_a/count_a)


#Find the smallest number usine None
smallest = None
print('before none')
for value in [9,41,12,3,74,15] :
    if smallest is None :
        smallest=value
    elif value < smallest :
        smallest=value
    print(smallest,value)
print('after none',smallest)
