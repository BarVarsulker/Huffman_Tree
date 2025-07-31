class Node:
    def __init__(self, count, right=None, left=None, root=None):
        self.left = left
        self.right = right
        self.root = root
        self.data = root
        self.count = count

    def joint(self, node):
        node3 = Node(self.count + node.count, self, node, self.count + node.count)
        return node3

    # inorder traversal
    # Left -> Root -> Right
    def inorder_traversal(self):
        res = []
        if self.left:
            res = res + self.left.inorder_traversal()
        res.append(self.data)
        if self.right:
            res = res + self.right.inorder_traversal()
        return res

    # preorder traversal
    # Root -> Left -> Right
    def preorder_traversal(self):
        res = []
        if self:
            res.append(self.data)
            if self.left:
                res = res + self.left.preorder_traversal()
            if self.right:
                res = res + self.right.preorder_traversal()
        return res


def find_huffman_code(tree, target, code=""):
    if tree.data == target:
        return code
    if tree.left:
        left_res = find_huffman_code(tree.left, target, code + "0")
        if left_res:
            return left_res
    if tree.right:
        right_res = find_huffman_code(tree.right, target, code + "1")
        if right_res:
            return right_res
    return None


def binary_to_chars(binary_str):
    # Split the binary string into chunks of 8 bits
    binary_chunks = [binary_str[i:i+7] for i in range(0, len(binary_str), 7)]

    # Convert each chunk to its corresponding character
    chars = ''.join(chr(int(chunk, 2)) if int(chunk, 2) != 127 else '0' for chunk in binary_chunks)

    return chars


if __name__ == "__main__":
    # Get user input for the file path
    file_path = input("Enter the path of the text file (if the file is in the directory, enter the file name): ")
    try:
        data = open(file_path, 'r')
        data_read = data.read()
        data_list = []
        data_tree = []
        flag = 0
        for x in data_read:
            data_list.append(x)
            for ls in data_tree:
                if ls[0] == x:
                    ls[1] += 1
                    flag = 1
            if flag == 0:
                data_tree.append([x, 1])
            else:
                flag = 0
        data_tree_sorted = sorted(data_tree, key=lambda val: val[1])
        nodes_list = []
        for i in range(len(data_tree_sorted)):
            nodes_list.append(Node(data_tree_sorted[i][1], None, None, data_tree_sorted[i][0]))
        while len(nodes_list) > 1:
            nodes_list.append(nodes_list[0].joint(nodes_list[1]))
            nodes_list.pop(0)
            nodes_list.pop(0)
            nodes_list = sorted(nodes_list, key=lambda x: x.count)
        dict = {}
        for i in range(len(data_tree_sorted)):
            dict[data_tree_sorted[i][0]] = find_huffman_code(nodes_list[0], data_tree_sorted[i][0])
        new_data = ""
        for x in data_read:
            new_data += dict[x]
        while len(new_data) % 7 != 0:
            new_data += '0'
        text = binary_to_chars(new_data)
        with open("compressed.txt", "w", encoding="ascii") as file:
            file.write(text)
            file.write("\n")
            file.write(f"{nodes_list[0].inorder_traversal()}")
            file.write("\n")
            file.write(f"{nodes_list[0].preorder_traversal()}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")