from   bag import Bag
import unittest  # use unittest.TestCase
import random    # use random.shuffle,random.randint

#random.shuffle(alist) mutates its alist argument, to be a random permutation
#random.randint(1,10)  returns a random number in the range 1-10 inclusive


class Test_Bag(unittest.TestCase):
    def setUp(self):
        self.alist = ['d','a','b','d','c','b','d']
        self.bag = Bag(self.alist)
        
    def test_len(self):
        self.assertEqual(len(self.bag), 7)
        random.shuffle(self.alist)
        length = len(self.bag)
#         random_num = random.randint(1, len(self.alist))
        for index in range(len(self.alist)):
            length -=1
            self.bag.remove(self.alist[index])
#             random.shuffle(self.alist)
            self.assertEqual(len(self.bag), length)
            index +1
    
         
    def test_unique(self):
        self.assertEqual(self.bag.unique(), 4)
        random.shuffle(self.alist)
        for i in range(len(self.alist)):
            self.bag.remove(self.alist[i])
            self.assertEqual(self.bag.unique(), len(set(self.bag)))

             
    def test_contains(self):
        self.assertTrue('a' in self.bag)
        self.assertTrue('d' in self.bag)
        self.assertTrue('c' in self.bag)
        self.assertTrue('x' not in self.bag)
        
    def test_count(self):
        self.assertEqual(self.bag.count('a'), 1)
        self.assertEqual(self.bag.count('b'), 2)
        self.assertEqual(self.bag.count('c'), 1)
        self.assertEqual(self.bag.count('d'), 3)
        self.assertEqual(self.bag.count('x'), 0)
        temp_counter = 8
        random.shuffle(self.alist)
        for i in self.alist:
            self.bag.remove(i)
            temp_counter -= 1
            self.assertEqual(len(self.bag), temp_counter-1)
    
    def test__eq__(self):
        result = [ ]
        for i in range(1, 1001):
            number = random.randint(1, 10)
            result.append(number)
        bag1 = Bag(result)
        random.shuffle(result)
        bag2 = Bag(result)
        self.assertEqual(bag1, bag2)
        self.assertNotEqual(bag1.remove(result[0]), bag2)
        
    def test_add(self):
        result = [ ]
        for i in range(1, 1001):
            number = random.randint(1, 10)
            result.append(number)
        bag1 = Bag(result)
        bag2 = Bag([])
        random.shuffle(result)
        for i in result:
            bag2.add(i)
        self.assertEqual(bag1, bag2)
        
    def test_remove(self):
        result = [ ]
        for i in range(1, 1001):
            number = random.randint(1, 10)
            result.append(number)
        bag1 = Bag(result)
        self.assertRaises(ValueError, result.remove,42)
        bag2 = Bag(result)
        random.shuffle(result)
        for num in result:
            bag2.add(num)
        for rnum in result:
            bag2.remove(rnum)
        self.assertEqual(bag1, bag2)