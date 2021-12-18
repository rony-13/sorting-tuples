import sys
item_no = input('Set the total number of tuples to insert in integer: ')

def sorting(list_of_tuples):
    list_of_tuples.sort()
    return list_of_tuples

try:
	item_no = int(item_no)
except Exception as err:
	print(str(err))
	sys.exit('Please insert in integer format, i.e. 1 or 5 or 7')

items = []
for i in range(item_no):
	item = input('Add comma seperated Name(String),Age (Int),Score (Int): ')
	item = item.split(',')
	if(len(item)>3):
		sys.exit('More than 3 items provided')
	try:
		item = (str(item[0]),int(item[1]),int(item[2]))
	except Exception as err:
		sys.exit(str(err))
	items.append(item)

print(f'Unsorted Inputs: {items}')
sorted_items = sorting(items)
print(f'Sorted Inputs: {sorted_items}')