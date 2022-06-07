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
            self.tail = self
            
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
            
        self.tail = temp.tail
        
        return self, temp.value
    
    def isEmpty(self):
        if self.value == None and self.next == None:
            return True
        
        return False
        
        
class Tree:
    def __init__(self, value : tuple[str, int]) -> None:
        self.val = value
        self.left = None
        self.right = None
    
    @classmethod
    def encodeTree(cls, root : "Tree", compress : bool = True) -> str:
        """Encode Tree Into a String

        Args:
            root (Tree): Tree Datastructures that want to encoded into a string
            compress (bool, optional): FLag to  compress the string. Defaults to True.

        Returns:
            str : Encoded Tree
        """
        
        
        # the queue seems can't handle none value, to get around put inside a tuple
        
        # encodedTree, queue = "", Queue((root)) # why this doesn't work?
        encodedTree, queue = "", Queue((root, 0, 0))  # why this work? WTFFFF!!!!
        
        
        while not queue.isEmpty():
            queue, (root, a_,b_) = queue.pop() 
            # queue, root = queue.pop()
            
            # if lvl != currLevel:
                # currLevel = lvl
                # NodePos, lastNodePos = 0, -1
            
            # encodedTree += "||" * ((Pos - lastNodePos) - 1) if Pos > lastNodePos else ""
            # lastNodePos = Pos # Update last position
            
            rootStr = "({},{})".format(root.val[0], root.val[1]) if root != None else ""
            
            encodedTree += "|{}".format(rootStr)

            if root != None:
                queue.insert((root.left, 0, 0))
                queue.insert((root.right, 0, 0))
                # queue.insert((root.left))
                # queue.insert((root.right))
                
            # NodePos += 1
            
        # remove trailing | if exist
        if encodedTree[-1] == "|":
            for i in range(len(encodedTree) - 1, 0, -1):
                if encodedTree[i - 1] != "|":
                    break
                
            encodedTree = encodedTree[:i]
            
        # Compressed the string
        if compress:
            # compressed repeated | into |n
            # ex : |(a, 3)||||||||||||(b, 17)|... -> |(a, 3)|12(b, 17)|...
            
            # | at the end isn't counted so begin counting at 1
            flag, count = False, 1
            
            encodedTree_compress = ""
            
            for i in range(len(encodedTree)):
                # encodedTree doens't have trailing |, so encodedTree[i + 1] is safe
                
                if encodedTree[i] == "|" and encodedTree[i + 1] != "(":
                    # begin counting repeated |
                    count += 1
                    flag = True
                    
                else:   
                    if flag:
                        encodedTree_compress += "|{}".format(count)
                        count = 1
                        flag = False
                        
                    else:
                        encodedTree_compress += encodedTree[i]
            
            encodedTree = encodedTree_compress
      
        return encodedTree
  
    @classmethod
    def decodeTree(cls, str : str, isCompress : bool = True):
        """Create a tree from an encoded tree in a string

        Args:
            str (str): Encoding of a tree
        """
        def uncompress(str):
            # Uncompress the encodedString
            # ex : |(a, 15)|14(b, 15)...
            
            uncompress_str, i = "", 0
            while i < len(str):
                if str[i] == "|" and str[i + 1] != "(":
                    # read the total repeated |
                    num = ""
                    
                    for j in range(i + 1, len(str)):
                        if str[j] == "(":
                            break
                        
                        num += str[j]
                        
                    num = int(num)
                    uncompress_str += "|" * num
                    i = j
                    
                else:
                    uncompress_str += str[i]
                    i += 1
                
            return uncompress_str
     
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
                
                elif str[i] == "," and (str[i + 1] != ","):
                    value.append(temp)
                    temp = ""
                    continue
                
                elif str[i] == "|":
                    value = None
                    break
                
                if flag:
                    temp += str[i]

            return value, i
        
        if isCompress:
            str = uncompress(str)
            
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

            if fnc_compare(val, self.heap[center]):
                # place val on the right side of center
                self.heap = self.heap[:center + 1] + [val] + self.heap[center + 1:]

            else:
                # place val on the right side of center
                self.heap = self.heap[:center] + [val] + self.heap[center:]

    
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
    
