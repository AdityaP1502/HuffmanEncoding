from collections import defaultdict
from Datastructures import Tree, minHeap
   
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
                encodeTable[root.val[0]] = encodedBits
                continue
                
            # if go left add "0" to encodedBits else add 1
            stack.append([root.left, encodedBits + "0"])
            stack.append([root.right, encodedBits + "1"])
            
        return encodeTable
    
    @classmethod
    def encode(cls, text : str) -> tuple[str, str]:
        """ Compress text using huffman encoding

        Args:
            text (str): a text
            
        Returns:
            tuple[str, str] : Tuple that contains the encoded message in bits and the encoded huffman Tree
        """
        def characterFrequency(text : str) -> dict:
            frequencyTable = defaultdict(int)
            for char in text:
                frequencyTable[char] += 1
                
            return frequencyTable
        
        def createHuffTree(FreqTable : minHeap):
            while len(freqTable.heap) > 1:
                # pick two minimum freq node and combine to create a new root
                min_1 = freqTable.pop()
                min_2 = freqTable.pop()

                root = Tree(["", min_1.val[1] + min_2.val[1]])

                root.left = min_1
                root.right = min_2

                freqTable.insert(root, lambda x, y: x.val[1] < y.val[1])
                
            return freqTable.heap[0]
    
        freqTable = characterFrequency(text)
        
        # change freqTable into 2D array
        freqTable_Array = []
        for (char, freq) in freqTable.items():
            freqTable_Array.append((char, freq))
             
        freqTable = minHeap.heapify(freqTable_Array)
        
        # change the entry in minheap into a tree
        for (i, elmt) in enumerate(freqTable.heap):
            freqTable.heap[i] = Tree(elmt)
        
        # create huff tree
        huffTree = createHuffTree(freqTable)
        
        # encode the tree
        encodedHuffTree = Tree.encodeTree(huffTree)
        
        # encode the message
        encodedTable = cls.TableFromTree(huffTree)
        encodedMessage = ""
        for char in text:
            encodedMessage += encodedTable[char]
        
        return encodedMessage, encodedHuffTree
        
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
    

                
            

    