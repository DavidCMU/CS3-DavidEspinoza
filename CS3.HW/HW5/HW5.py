import heapq
import os

class huffman_Node:
    def __init__ (self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman(text):
    freqencies = {}
    for char in text:
        freqencies[char] = freqencies.get(char, 0) +1
    
    priority_queue = []
    for char, freq in freqencies.items():
        new_node = huffman_Node(char, freq)
        priority_queue.append(new_node)
    
    heapq.heapify(priority_queue)
    
    while (len(priority_queue) > 1):
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)

        combined = huffman_Node(None, left_node.freq + right_node.freq)
        combined.left = left_node
        combined.right = right_node

        heapq.heappush(priority_queue, combined)

    if len(priority_queue) == 0:
        return None
    
    return priority_queue[0]

def huffman_codes(root):
    if root is None:
        return{}
    codes= {}
    stack = [(root,"")]

    while len(stack) > 0:
        node, current_code = stack.pop()

        if node.char is not None:
            codes[node.char] = current_code
        
        if node.right:
            stack.append((node.right, current_code + "1"))
        
        if node.left:
            stack.append((node.left, current_code + "0"))
    return codes

def encode(text, codes):
    binary_result = ""

    for char in text:
        binary_code = codes[char]
        binary_result = binary_result + binary_code
    return binary_result

def decode(binary_string, root):
    result = ""
    curr = root
    for bit in binary_string:
        if bit == '0':
            curr = curr.left
        else:
            curr = curr.right

        if curr.left is None and curr.right is None:
            result += curr.char
            curr = root
    return result

def main():
    text_choice = input("Enter 's' in order to type your own string or 't' for a text file you would like to use for huffman\n")
    
    if text_choice == 't':
        file_choice = input("please enter file name\n")
        if os.path.exists(file_choice):
            with open(file_choice, 'r') as f:
                input_text = f.read()
        else:
            print("file not found")
    else:
        input_text = input("Enter your string: ")

    if not input_text:
        return

    root = build_huffman(input_text)
    codes = huffman_codes(root)
    encoded = encode(input_text, codes)
    decoded = decode(encoded, root)
    
    og_bits = len(input_text) *8
    com_bits = len(encoded)
    if com_bits > 0:
        ratio = og_bits / com_bits
    else:
        ratio = 0
    

    print(f"\nInput: {input_text}")
    print("\nHuffman Codes:")
    for c, code in codes.items():
        char_label = f"'{c}'" if c != " " else "space"
        print(f"{char_label}: {code}")
    print(f"\nEncoded String: {encoded}")
    print(f"Decoded String: {decoded}")
    print(f"Orignal size: {og_bits}")
    print(f"Compressed size: {og_bits}")
    print(f"Ratio size: {ratio}")


        
if __name__ == "__main__":
    main()