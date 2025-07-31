import ast
class Node:
    def __init__(self, root, right=None, left=None):
        self.left = left
        self.right = right
        self.root = root
        self.data = root


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]  # Get the value of the root node without modifying preorder
    root = Node(root_val)

    root_index = inorder.index(root_val)

    # Make copies of preorder for the recursive calls
    left_preorder = preorder[1:root_index + 1]
    right_preorder = preorder[root_index + 1:]

    root.left = build_tree(left_preorder, inorder[:root_index])
    root.right = build_tree(right_preorder, inorder[root_index + 1:])

    return root


def decode_huffman(encoded_str, root):
    decoded_str = ""
    node = root
    for bit in encoded_str:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        # Check if node is a leaf node
        if node.left is None and node.right is None:
            decoded_str += node.root
            node = root

    return decoded_str


if __name__ == "__main__":
    # Get user input for the file path
    file_path = input("Enter the path of the text file (if the file is in the directory, enter the file name): ")
    try:
        with open(file_path, 'r', encoding="ascii") as file:
            data = file.readlines()
            inorder = ast.literal_eval(data[-2])
            preorder = ast.literal_eval(data[-1])
            data = data[:-2]
        binary_strings = ''
        for string in data:
            binary_representation = ''.join(format(ord(byte), '07b') for byte in string)
            binary_strings += binary_representation
        tree = build_tree(preorder, inorder)
        txt = decode_huffman(binary_strings, tree)
        with open("decompressed.txt", "w") as file:
            file.write(txt)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")