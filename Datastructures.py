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