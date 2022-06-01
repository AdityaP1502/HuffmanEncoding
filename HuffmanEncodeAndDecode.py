from collections import defaultdict
from random import randint
from Datastructures import Tree, Queue, minHeap
   
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
    