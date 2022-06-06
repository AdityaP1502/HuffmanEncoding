"""
                                                                        Testing Module
"""

from Datastructures import Queue, Tree, minHeap
from random import randint
from HuffmanEncodeAndDecode import HuffmanEncoding
from memory_profiler import profile
from time import perf_counter

class Testing:
    """
    Class for testing performance and creating random testcase to test the algorithm
    """
    
    def timeis(fnc):
        def timeit(*args, **kwargs):
            start = perf_counter()
            fnc(*args, **kwargs)
            end = perf_counter()

            print((end - start) * 1000, 'ms')
            
        return timeit
    
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
    
    @classmethod
    def measurePerformance(cls, testCase : str) -> str:
        """Measure the memory used in creating huffman encoded message

        Args:
            testCase (str): Testcase to measure the performance

        Returns:
            str: Memory Consumption Report
        """
        @profile
        def measureMemory():
            encodedMessage, huffTree = HuffmanEncoding.encode(testCase)
        
        @cls.timeis
        def measureTime():
            encodedMessage, huffTree = HuffmanEncoding.encode(testCase)
        
        print("Performance Report")
        
        # can't seem to finish for a large text
        # print("Memory Report")
        # measureMemory()
        
        print("Time Report")
        measureTime()
        
    
    
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
    
    text = """An aphrodisiac is a food or drug that arouses sexual instinct, brings on desire, or increases sexual pleasure or performance"""
    # text = "Bekasiishot"
    
    encodedMessage, huffTree = HuffmanEncoding.encode(text)
    print(encodedMessage, huffTree)
    
    # # Measure time and memory consumption
    # # Testing.measurePerformance(text)
    
    # decode the message back
    originalMessage = HuffmanEncoding.decode(encodedMessage, huffTree)
    print(originalMessage)
    
    # test whether we got the message right
    print(originalMessage == text)
   
   
    # tree = "|(,124)|(,50)|(,74)|(,23)|(,27)|(,34)|(,40)|(e,11)|(s,12)|(r,12)|(,15)|(,16)|(,18)|( ,19)|(,21)|||||||(n,7)|(,8)|(,8)|(i,8)|(,9)|(o,9)|||(a,10)|(,11)||||||||||||||||||(t,4)|(c,4)|(,4)|(,4)|||(d,4)|(u,5)|||||||||||(,5)|(,6)||||||||(g,2)|(f,2)|(,,2)|(x,2)|||||||||||||||||||||||(h,2)|(l,3)|(,3)|(p,3)||||||||||||||||||||||||||||||||||(A,1)|(,2)||||||||||||||||||||||||||||||||||||||(m,1)|(b,1)"
    # myTree = Tree.decodeTree(tree)
    # encodeTree = Tree.encodeTree(myTree)
    # print(tree)
    # print(encodeTree)
    