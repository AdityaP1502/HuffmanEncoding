"""
                                        Testing Module
"""

from Datastructures import Queue, Tree, minHeap
from random import randint
from HuffmanEncodeAndDecode import HuffmanEncoding

class Testing:
    """
    Class for creating random testcase to test the algorithm
    """
    @classmethod
    def createRandomTree(cls, n : int) -> Tree:
        """Create Random Tree

        Args:
            n (int): # Non - Null Element in the Tree
        Returns:
            Tree : Test Tree
        """
        
        vals = [randint(0, 1000) for i in range(n)]
        chars = [chr(randint(32, 126)) for i in range(n)]

        # create n randon pair of char and integer
        arr = list(zip(chars, vals))
        
        # initialize the main root
        root = Tree(arr[0])
        temp = root
        del arr[0]
        
        stack = [root]
        
        i = 0
        
        while len(arr) > 0:
            root = stack.pop()
            
            # randomize the null location
            null = randint(0, 1)
            if null == 1:
                # left node is null
                root.right = Tree(arr[i])
                del arr[i]
                stack.append(root.right)
                 
            else:
                root.left = Tree(arr[i])
                del arr[i]
                
                stack.append(root.left)
                
                null = randint(0, 1)
                
                if len(arr) == 0:
                    break
                
                if null == 0:
                    root.right = Tree(arr[i])
                    del arr[i]
                    
                    stack.append(root.right)
                             
        return temp