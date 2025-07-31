# Huffman Tree Compression in Python

## Overview

This project implements the **Huffman coding algorithm** in Python for text compression and decompression using a **Huffman tree**. Huffman coding is a lossless data compression algorithm that assigns variable-length binary codes to input characters, with shorter codes for more frequent characters.

The project includes:

- Building the Huffman tree from text input
- Encoding the text into a compressed binary format
- Decoding the binary data back into the original text
- Optionally exporting and reconstructing the tree structure using `ast`

## Features

- Frequency analysis of characters in input
- Priority queue (heap) for tree construction
- Dictionary generation for encoding
- Binary serialization of encoded data
- Tree reconstruction using:
  - Serialized structure + leaf order
  - Preorder traversal with markers (internal/leaf nodes)
  - AST (Abstract Syntax Tree) for human-readable or structured representation

> 📄 For educational purposes. Focus is on understanding compression logic and tree structure.

## Tree Reconstruction Methods

Several strategies are included for reconstructing the Huffman tree during decompression:

1. **Structure + Leaf List**  
   Save the tree shape as a binary string (`1` for internal node, `0` for leaf) and a list of leaf characters. Rebuild the tree recursively by consuming both.

2. **Preorder Encoding**  
   Perform a preorder traversal and store each node with a marker (e.g., `L:char` for leaf, `I` for internal). Reconstruct using recursive parsing.

3. **AST-Based Serialization**  
   Store the tree using Python’s `ast` module, allowing it to be saved as a structured representation (like nested tuples or expression trees), and parsed back safely using `ast.literal_eval`.

## What Does the Huffman Algorithm Do?

The Huffman algorithm minimizes the average length of codes used to represent characters, given their frequency in the input text.

**Steps:**
1. Count frequency of each character in input.
2. Build a binary tree where each leaf is a character and internal nodes represent combined frequencies.
3. Traverse the tree to assign binary codes:  
   - Left = 0  
   - Right = 1
4. Replace characters in text with their binary codes to create a compressed version.
5. To decompress, traverse the tree according to bits until reaching a leaf node.

## Example

**Original text:**
hello huffman

**Encoded binary:**
101010011001010...

## Usage

```bash
python compression.py 
python decompression.py
