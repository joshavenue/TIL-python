for x in range(1,11):
	for y in range(1,11):
		print('{} * {} = {}'.format(x,y,x*y))
    
##-----------------------------------------------##
list_in_list = [[1,2,3],[4,5,6],[7,8,9]]

for list in list_in_list:
	for x in list:
		print(x,end=' ')
##-----------------------------------------------##

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

for x in my_range(1, 10, 0.5):
    print(x)
