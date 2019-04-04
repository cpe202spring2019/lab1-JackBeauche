
def max_list_iter(int_list):  # must use iteration not recursion
#   finds the max of a list of numbers and returns the value (not the index)
#   If int_list is empty, returns None. If list is None, raises ValueError

    # Check if list is None:
    if (type(int_list) == type(None)):
        raise ValueError
    # Check if int_list is empty
    elif (len(int_list) == 0):
        return(None)
    # Process list iteratively if both checks fail
    else:
        MaxVal = int_list[0] # Assume MaxVal is first value
        
        for i in int_list:
            if i > MaxVal:
                MaxVal = i
        return(MaxVal)				
    pass

def reverse_rec(int_list):   # must use recursion
#   """recursively reverses a list of numbers and returns the reversed list
#   If list is None, raises ValueError"""
   pass

def bin_search(target, low, high, int_list):  # must use recursion
#   """searches for target in int_list[low..high] and returns index if found
#   If target is not found returns None. If list is None, raises ValueError """
   pass

if __name__ == '__main__':
    max_list_iter(None)