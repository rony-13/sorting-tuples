import sys

def sorting(list_of_tuples):
    print(f'Unsorted Inputs: {list_of_tuples}')
    list_of_tuples.sort()
    print(f'Sorted Inputs: {list_of_tuples}')

if __name__ == "__main__":
    # Get how much inputs will be provided from command line
    item_no = input('Set the total number of tuples to insert in integer: ')
    # Handle if wrong input type provided
    try:
        item_no = int(item_no)
    except Exception as err:
        print(str(err))
        sys.exit('Please insert in integer format, i.e. 1 or 5 or 7')

    items = []
    for i in range(item_no):
        item = input('Add comma seperated Name(String),Age (Int),Score (Int): ')
        item = item.split(',')

        # Handle if more items provided rather Name,Age,Score
        if(len(item)>3):
            sys.exit('More than 3 items provided')

        # Convert to accurate types
        try:
            item = (str(item[0]),int(item[1]),int(item[2]))
        except Exception as err:
            sys.exit(str(err))
        items.append(item)

    sorting(items)