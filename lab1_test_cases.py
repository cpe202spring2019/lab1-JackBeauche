import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

        emptylist = [] #empty list should return None
        self.assertEqual(max_list_iter(emptylist), None)

        worstcase = [1,2,3,4,5] # Worst case occurs when max value is the last value
        self.assertEqual(max_list_iter(worstcase), 5)
        
        #normal test cases with max value at different points
        MaxIdx0 = [5,1,2,3,4]
        MaxIdx1 = [1,5,2,3,4]
        MaxIdx2 = [1,2,5,3,4]
        MaxIdx3 = [1,2,3,5,4]
        self.assertEqual(max_list_iter(MaxIdx0), 5)
        self.assertEqual(max_list_iter(MaxIdx1), 5)
        self.assertEqual(max_list_iter(MaxIdx2), 5)
        self.assertEqual(max_list_iter(MaxIdx3), 5)
        

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) # test odd length list and the inverse list
        self.assertEqual(reverse_rec([3,2,1]),[1,2,3])
        
        self.assertEqual(reverse_rec([0,1,2,3]), [3,2,1,0]) # test even length list and the inverse list
        self.assertEqual(reverse_rec([3,2,1,0]), [0,1,2,3])
        
        self.assertEqual(reverse_rec([]), []) #test empty list
        
        with self.assertRaises(ValueError): #test None list with ValueError
            reverse_rec(None)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,5,6,7,8,9,10] # value = index for this list 
        low = 0
        high = len(list_val)-1
        for i in list_val: # test that we can find every value in the list
            self.assertEqual(bin_search(i, low, len(list_val)-1, list_val), i )
            
        self.assertEqual(bin_search(20, 0, len(list_val)-1, list_val), None ) # target is not in the list
        self.assertEqual(bin_search(0, len(list_val), low, list_val), None ) # Bad low & high = same result as target not being found
        self.assertEqual(bin_search(4, 5, len(list_val)-1, list_val), None ) # Search for 4 in upper half of List ([5,6,7,8,9,10]) = not found
        self.assertEqual(bin_search(9, low, 5, list_val), None ) # Search for 9 in lower half of List ([0,1,2,3,4,5]) = not found

if __name__ == "__main__":
        unittest.main()

    
