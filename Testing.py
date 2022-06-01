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
    
if __name__ == "__main__":
    # testTree = Testing.createRandomTree(10)
    # testEncodedTree = Tree.encodeTree(testTree)
    # print(testEncodedTree)
    
    # testEncodedTree = "|(j,25)||(S,584)||(~,46)||(>,611)||(:,723)|(%,614)|||(a,235)|(Q,392)||(,,671)|(V,773)"
    # testTreeDecoded = Tree.decodeTree(testEncodedTree)
    # print()
    
    # arr = [1, 2, 3]
    # queue = Queue()
    
    # for i in range(len(arr)):
        # queue.insert(arr[i])
        
    # for i in range(len(arr)):
        # queue, elmt = queue.pop()
        # print(elmt)
        
    # test for minheap
    # arr = [["a", 1], ["c", 3], ["f", 3], ["g", 10], ["e", 2]]
    # arr = minHeap.heapify(arr)
    # for (i, elmt) in enumerate(arr.heap):
        # arr.heap[i] = Tree(elmt)    
    
    # newArr = [["", 3], ["", 11], ["", -1], ["", 4], ["", 6]]
    # for elmt in newArr:
        # node = Tree(elmt)
        # arr.insert(node, lambda x, y: x.val[1] < y.val[1])
        
    # print()  
    # for elmt in arr.heap:
        # print(elmt.val)
    
    text = "Hello, my name is KNTL PAPAPAPA. Lived in NIHON, Hobby is staring at a wall while thinking about life decisions."
    encodedMessage, huffTree = HuffmanEncoding.encode(text)
    print(encodedMessage)