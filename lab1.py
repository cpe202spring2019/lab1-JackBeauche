
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
            if i > MaxVal: # Update MaxVal if an item is larger
                MaxVal = i
        return(MaxVal)				
    pass

def reverse_rec(int_list):   # must use recursion
#   """recursively reverses a list of numbers and returns the reversed list
#   If list is None, raises ValueError"""
    if(type(int_list) == type(None)):
        raise ValueError
    elif(len(int_list) == 0):
        return(int_list)
    else:
        return(reverse_rec(int_list[1:]) + int_list[0:1])   
    pass

def bin_search(target, low, high, int_list):  # must use recursion
#   """searches for target in int_list[low..high] and returns index if found
#   If target is not found returns None. If list is None, raises ValueError """
    if(type(int_list) == type(None)):
        raise ValueError
    elif( low <= high):
    
        mid = (low + high)//2 # mid point is defined
         
        if(target == int_list[mid]): # return mid if target is found
            return(mid)
        elif(target < int_list[mid]): # can search only the lower half of the list, since target is not found, we decrease 1 from mid and that is new high
            return(bin_search(target, low, mid - 1, int_list))
        else:
            return(bin_search(target, mid + 1, high, int_list)) # can search only the upper half of the list, since target is not found, we increase 1 from mid and that is new low 
    else:
        return(None) # target is not found in list
    pass

if __name__ == '__main__':
    max_list_iter(None)