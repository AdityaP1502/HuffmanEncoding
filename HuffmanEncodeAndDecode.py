from collections import defaultdict
import enum
from random import randint

class Queue:
    def __init__(self, value : any = None) -> None:
        self.value = value
        self.next = None
        self.tail = None
       
    def insert(self, value : any):
        """Insert element into a queue

        Args:
            value (any): value that want to be inserted in the queue
        """
        
        if self.value == None:
            self.value = value
            self.next = None
            self.tail = None
            
        elif self.tail == None:
            tail = Queue(value)
            self.next = tail
            self.tail = tail
            
        else:
            newTail = Queue(value)
            self.tail.next = newTail
            self.tail = newTail
            
    def pop(self) -> any:
        """Get the first element in the queue

        Returns:
            any : first element in the queue
        """
        temp = self
        self = self.next
        
        if self == None:
            self = Queue()
        
        return self, temp.value
        
        
class Tree:
    def __init__(self, value : tuple[str, int]) -> None:
        self.val = value
        self.left = None
        self.right = None
    
    @classmethod
    def encodeTree(cls, root : "Tree"):
        """Encode tree into a string

        Args:
            root (Tree): An object to tree
        """
        
        encodedTree, stack = "", [root]
        
        while len(stack) != 0:
            root = stack.pop()
            
            rootStr = "({},{})".format(root.val[0], root.val[1]) if root != None else ""
            
            encodedTree += "|{}".format(rootStr)

            if root != None:
                stack.append(root.right)
                stack.append(root.left)
            
        # remove trailing |
        for i in range(len(encodedTree) - 1, 0, -1):
            if encodedTree[i - 1] != "|":
                break
            
                
        return encodedTree[:i]
        
        
    @classmethod
    def decodeTree(cls, str : str):
        """Create a tree from an encoded tree in a string

        Args:
            str (str): Encoding of a tree
        """
        def readVals(start : int, str : str):
            # read the vals in string
            value = []
            temp = ""
            flag = False
            for i in range(start + 1, len(str)):
                if str[i] == "(" and not flag:
                    flag = True
                    continue
                    
                elif str[i] == ")" and str[i - 1] != "(":
                    value.append(int(temp))
                    break
                
                elif str[i] == "," and (str[i - 1] != "(" or str[i - 2] == "("):
                    value.append(temp)
                    temp = ""
                    continue
                
                elif str[i] == "|":
                    value = None
                    break
                
                if flag:
                    temp += str[i]

            return value, i
        
        i = 0
        # get value for main root
        value, i = readVals(0, str)
        
        root = Tree(value)
        temp = root
        
        queue = Queue(root)
        
        while i < len(str):
            if str[i] == "|":
                queue, root = queue.pop()
                
                # get value for left child
                value, i = readVals(i, str)
                if value != None:
                    root.left = Tree(value)
                    queue.insert(root.left)
                    
                else:
                    root.left = None
                    
                i = i + 1 if value != None else i
                
                if i > len(str) - 1:
                    break
                
                # get value for right child
                value, i = readVals(i, str)
                root.right = Tree(value)
                if value != None:
                    root.right = Tree(value)
                    queue.insert(root.right)
                    
                else:
                    root.right = None
                    
            else:       
                i += 1

        return temp
                    
                    

class minHeap:
    """
    Heap data structures using array. The array, therefore, is sorted in decreasing order
    """
    def __init__(self) -> None:
        self.heap = []
        
    def insert(self, val : any, fnc_compare :  "function") -> None:
        """ Insert Value into minHeap. The minimum value located at idx -1

        Args:
            val (any): Value that want to be inserted to the minHeap 
            fnc_compare(function) : function to compare value in order to determine the location of val in the heap
        """
        if len(self.heap) == 0:
            self.heap.append(val)

        elif fnc_compare(val, self.heap[-1]):
            self.heap = self.heap + [val]
            
        elif not fnc_compare(val, self.heap[0]): # not val[1] < self.heap[0][1]
            self.heap = [val] + self.heap

        else:
            start, end = 0, len(self.heap) - 1
            # Binary search to find the correct placement of the value
            while start <= end:
                center = start + (end - start) // 2
                if fnc_compare(self.heap[center], val):
                    # val[1] is greatr than center, therefore its place is located on the left side of center
                    end = center - 1

                else:
                    # val[1] is smaller, therefore is on the right side of center
                    start = center + 1

            if fnc_compare(self.heap[center], val):
                # place val on the left side
                self.heap = self.heap[:center] + [val] + self.heap[center:]

            else:
                # place val on the right side of center
                self.heap = self.heap[:center + 1] + [val] + self.heap[center + 1:]

    
    def pop(self) -> any:
        """Remove the minimum value in the heap

        Returns:
            any : return the minimum value in the heap
        """
        return self.heap.pop()
    
    @classmethod
    def heapify(cls, arr : list[str, int]) -> "minHeap":
        # create a heap from 
        arr.sort(reverse = True, key = lambda x:x[1])
        heap = cls()
        heap.heap = arr
        return heap
    
       
class HuffmanEncoding():
    @classmethod
    def TableFromTree(cls, huffTree : Tree) -> dict:
        """Generate a encodedTable from huffman Tree

        Args:
            encodeTree (Tree): Tree Used in Creating the Huffman Encoding

        Returns:
            dict: Conversion Table
        """
        encodeTable = {}
        
        # tranverse the tree
        stack = [(huffTree, "")]
        
        # for node that has val[0] == "", there always exist two child,
        while len(stack) > 0:
            root, encodedBits = stack.pop()
            # if val[0] in root isn't "" then add entry to table
            if root.val[0] != "":
                dict[root.val[0]] = encodedBits
                continue
                
            # if go left add "0" to encodedBits else add 1
            stack.append([root.left, encodedBits + "0"])
            stack.append([root.right, encodedBits + "1"])
            
        return encodeTable
    
    @classmethod
    def encode(cls, text : str) -> str:
        """ Compress text using huffman encoding

        Args:
            text (str): a text
            
        Returns:
            str : encoded text in bits
        """
        def characterFrequency(text : str) -> dict:
            frequencyTable = defaultdict(int)
            for char in text:
                dict[char] += 1
                
            return frequencyTable
        
        def createHuffTree(FreqTable : minHeap):
            while len(freqTable.heap) > 1:
                # pick two minimum freq node and combine to create a new root
                min_1 = freqTable.pop()
                min_2 = freqTable.pop()

                root = Tree(["", min_1.val[1] + min_2.val[1]])

                root.left = min_1
                root.right = min_2

                freqTable.insert(root)
                
            return freqTable.heap[0]
    
        freqTable = list(characterFrequency(text))
        freqTable = minHeap.heapify(freqTable)
        
        # change the entry in minheap into a tree
        for (i, elmt) in enumerate(freqTable.heap):
            freqTable[i] = Tree(elmt)
        
        # create huff tree
        huffTree = createHuffTree(freqTable)
        
        # encode 
        encodedTable = cls.TableFromTree(huffTree)
        encodedMessage = ""
        for char in text:
            encodedMessage += encodedTable[char]
            
        return encodedMessage
        
    @classmethod
    def decode(cls, encodedText : str, table : dict) -> str:
        """Get the original message back from the encoded text

        Args:
            encodedText (str): Encoded message in bits using huffman encoding
            table (dict): Conversion Table

        Returns:
            str: Original message
        """
        pass
    
class Testing:
    @classmethod
    def createRandomTree(cls, n : int):
        vals = [randint(0, 1000) for i in range(n)]
        chars = [chr(randint(32, 126)) for i in range(n)]
        
        arr = list(zip(chars, vals))
        
        root = Tree(arr[0])
        temp = root
        del arr[0]
        
        stack = [root]
        
        i = 0
        
        while len(arr) > 0:
            root = stack.pop()
            
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
    
    pass
    