##
## ***************************************************
## Shayan Syed (20956352)
## CS 116 Spring 2022
## Assignment 10, Problem 3
## ***************************************************
##


#import check

class BSTNode:
  '''
  Fields:
     val (Int)
     lchild (anyof BSTNode None)
     rchild (anyof BSTNode None)
     
  Requires:
     Every val of each node in lchild is less than val
     Every val of each node in rchild is greater than val
  '''
  
  def __init__(self, val, lchild, rchild):
    '''
    Constructor: Create a BSTNode by calling BSTNode(value, left, right)
   
    Effects: Mutates self
    '''
    self.val = val
    self.lchild = lchild
    self.rchild = rchild
  
  def __eq__(self, other):
    '''
    Returns True if the BSTNodes are equal
    
    __eq__: BSTNode Any -> Bool
    '''
    return isinstance(other, BSTNode) and\
      self.val == other.val and\
      self.lchild == other.lchild and\
      self.rchild == other.rchild
    pass
  
  def __repr__(self):
    '''
    Returns a representation of the BSTNode object
    
    __repr__: BSTNode -> Str
    '''
    if self.lchild == None and self.rchild == None:
      return str(self.val)
      self.lchild == ''
    if self.lchild == None:
      return str(self.val) + ',' + str(self.rchild)
    if self.rchild == None:
      return str(self.val) + ',' + str(self.lchild)
    else:
      s = "{0.val},{0.lchild},{0.rchild}"
      return s.format(self)
  
  
def contains(root, item):
  '''
  Consumes a BSTNode root and an item of any data type and returns True if item
  is in the Binary Search Tree and False otherwise
  
  contains: BSTNode Int -> Bool
  
  Examples:
    ExB1 = BSTNode(509464, None, None)
    contains(ExB1, 509464) => True
    
    ExB2 = BSTNode(37, BSTNode(9, None, None), BSTNode(47, None, None))
    contains(ExB2, 123) => False
    contains(ExB2, 37) => True
  '''
  if root == None:
    return False
  elif item == root.val:
    return True
  elif item < root.val:
    return contains(root.lchild, item)
  elif item > root.val:
    return contains(root.rchild, item)
    

'''
##Basic Tests
B = BSTNode(123, BSTNode(3, None, None), None)
check.expect("MarkUs Basic Test __init__", B.val == 123, True)
check.expect("MarkUs Basic Test __init__", B.lchild.val == 3, True)
check.expect("MarkUs Basic Test __init__", B.rchild == None, True)
check.expect("MarkUs Basic Test __init__", B.lchild.lchild == None, True)
check.expect("MarkUs Basic Test __init__", B.lchild.rchild == None, True)

B1 = BSTNode(388, None, None)
B2 = BSTNode(388, None, None)
check.expect("MarkUs Basic Test __eq__", B1==B2, True)

B1 = BSTNode(2, None, None)
check.set_print_exact("2")
check.expect("MarkUs Basic Test __repr__", print(B1), None)

M = BSTNode(388, None, None)
check.expect("MarkUs Basic Test", contains(M, 388), True)

##Examples as Tests
ExB1 = BSTNode(509464, None, None)
check.expect("sample 1", contains(ExB1, 509464), True)

ExB2 = BSTNode(37, BSTNode(9, None, None), BSTNode(47, None, None))
check.expect("sample 2", contains(ExB2, 123), False)
check.expect("sample 3", contains(ExB2, 37), True)

##Other Tests
TestB = BSTNode(10, BSTNode(8, BSTNode(4, None, BSTNode(6, \
BSTNode(5, None, None), BSTNode(7, None, None))), None), BSTNode(18, \
BSTNode(17, None, None), BSTNode(19, None, None)))
check.expect("furthest num", contains(TestB, 7), True)
check.expect("doesnt exist", contains(TestB, 43), False)
check.expect("has two children", contains(TestB, 18), True)
'''
